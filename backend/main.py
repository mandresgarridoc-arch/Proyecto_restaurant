<<<<<<< HEAD
#FastApi framework que crea el servidor, httpException envia errores como error 500 si la base de datos falla
from fastapi import FastAPI, HTTPException

from pymongo import MongoClient 
from dotenv import load_dotenv #lee archivos secretos .env y carga las contraseñas
from bson import ObjectId #ayuda a convertir los id de mongo en texto para que el navegador lospueda leer
import os

# 1. Configuración inicial

load_dotenv() #carga las variables del archivo .env
app = FastAPI(title="RestoManager API") #recibe las peticiones

# 2. Conexión segura a MongoDB Atlas

MONGO_URI = os.getenv("MONGO_URI") #trae la direccion del cluster de atlas
cliente_mongo = MongoClient(MONGO_URI) #conecta con la nube
db = cliente_mongo["resto_manager_db"] # Nombre de la base de datos

# 3. Endpoint: Listar todos los platos de la carta
@app.get("/carta") #a esto se le llama decorador, dice si alguien pide la /carta ehecuta esto
def obtener_carta():
    try:
        # Convertimos los documentos de Mongo a una lista que FastAPI entiende
        lista_platos = list(db["carta"].find()) #busca todos los documentos dentro de la coleccion carta
        
        # Convertimos el ID (que es tipo BSON) a un string para que JSON lo acepte
        for plato in lista_platos:
            plato["_id"] = str(plato["_id"]) #con str convertimos los id en texto
            
        return {"carta": lista_platos}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 4. Endpoint: Agregar un plato nuevo (CRUD - Create)
@app.post("/carta") #post enviamos informacion para guardarla
def crear_plato(plato: dict): 
    resultado = db["carta"].insert_one(plato) #envia documento a mongo atlas
    #devuelve un mensaje de confirmacion 
    return {"mensaje": "Plato agregado", "id": str(resultado.inserted_id)}


