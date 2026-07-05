# FastAPI framework crea el servidor, httpException envía errores
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient 
from dotenv import load_dotenv  # lee archivos secretos .env y carga las credenciales
from bson import ObjectId       # ayuda a convertir los id de mongo en texto
import os

# 1. Configuración inicial
load_dotenv()  # carga las variables del archivo .env
app = FastAPI(title="RestoManager API")  # recibe las peticiones
#Ejemplo para mostrar al usuario que la API está corriendo, y que puede ir a la documentación interactiva
@app.get("/", summary="Ruta de inicio")
def inicio():
    return {"mensaje": "¡Bienvenido a la API de SisGes! Ve a http://127.0.0.1:8000/docs para ver la documentación interactiva."}

# 2. Conexión segura a MongoDB Atlas
MONGO_URI = os.getenv("MONGO_URI")  # trae la dirección del clúster de atlas
cliente_mongo = MongoClient(MONGO_URI)  # conecta con la nube
db = cliente_mongo["resto_manager_db"]  # Nombre de la base de datos de SisGes

# Formatea los documentos de MongoDB para que sean legibles por JSON y FastAPI
def serializar_documento(doc) -> dict:
    if not doc:
        return None
    # convierte el objectid de mongo a una id de texto(str) para que el navegador pueda leerlo
    doc["id"] = str(doc["_id"])
    del doc["_id"]  # elimina el campo _id oriiginal para que no se duplique
    return doc #retorna el documento ya formateado 


# ==========================================
# RUTAS DE LA SECCIÓN DEL MESERO (RF-01)
# ==========================================

@app.get("/mesas", summary="Obtener el estado de todas las mesas en tiempo real")
def obtener_mesas():
    try:
        # Buscamos todas las mesas en la colección
        cursor_mesas = db.mesas.find()
        lista_mesas = []
        
        for mesa in cursor_mesas:
            lista_mesas.append(serializar_documento(mesa))
            
        # CONTROL DE SEGURIDAD INTELEGENTE:
        # Si la base de datos está recién creada y vacía, poblamos automáticamente
        # unas mesas de prueba para que React no falle al renderizar.
        if len(lista_mesas) == 0:
            mesas_prueba = [
                {"numero": 1, "capacidad": 2, "estado": "disponible"},
                {"numero": 2, "capacidad": 4, "estado": "disponible"},
                {"numero": 3, "capacidad": 4, "estado": "ocupada"},
                {"numero": 4, "capacidad": 6, "estado": "reservada"}
            ]
            db.mesas.insert_many(mesas_prueba)
            # Reconsultamos de nuevo ya con datos reales guardados
            return [serializar_documento(m) for m in db.mesas.find()]
            
        return lista_mesas
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la base de datos: {str(e)}")


@app.get("/menu", summary="Ver platos y bebidas disponibles en la carta")
def obtener_menu():
    try:
        # Traemos solo los productos que tengan disponible: True
        cursor_menu = db.menu.find({"disponible": True})
        lista_productos = []
        
        for producto in cursor_menu:
            lista_productos.append(serializar_documento(producto))
            
        # Poblado automático inicial para pruebas del menú
        if len(lista_productos) == 0:
            menu_prueba = [
                {"nombre": "Ceviche Mixto", "categoria": "plato", "precio": 12000, "disponible": True},
                {"nombre": "Lomo Saltado", "categoria": "plato", "precio": 14000, "disponible": True},
                {"nombre": "Pisco Sour", "categoria": "bebida", "precio": 5000, "disponible": True},
                {"nombre": "Limonada Menta Jengibre", "categoria": "bebida", "precio": 3500, "disponible": True}
            ]
            db.menu.insert_many(menu_prueba)
            return [serializar_documento(p) for p in db.menu.find({"disponible": True})]
            
        return lista_productos
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener el menú: {str(e)}")