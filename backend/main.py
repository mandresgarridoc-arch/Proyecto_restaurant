from fastapi import FastAPI, HTTPException
from pymongo import MongoClient 
from dotenv import load_dotenv
import os

# IMPORTAMOS NUESTROS OBJETOS DESDE LAS OTRAS CARPETAS
from dtos.menu_dto import PlatoDTO
from daos.menu_dao import MenuDAO

# con load_dotenv() cargamos las variables de entorno del archivo .env
load_dotenv() 
#crea el servidor de fastapi
app = FastAPI(title="SisGes API") 

# Conexión Global
MONGO_URI = os.getenv("MONGO_URI") 
cliente_mongo = MongoClient(MONGO_URI) 
db = cliente_mongo["resto_manager_db"]

# al instanciar MenuDAO le pasamos la conexion a la base de datos para que pueda usarla en sus metodos
#el (db) es el parametro que le permite a la clase MenuDAO usar la conexion a la base de datos en sus metodos
menu_dao = MenuDAO(db)

# 1. Endpoint: Listar todos los platos de la carta
@app.get("/admin/menu") # decorador que indica que este metodo se ejecuta cuando alguien hace un GET(obtener datos) a /admin/menu
def ver_carta_completa():
    try:
        return menu_dao.obtener_platos()# llama al metodo obtener_platos de la clase MenuDAO para traer los platos
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/admin/menu") # decorador que indica que este metodo se ejecuta cuando alguien hace un POST(enviar datos) a /admin/menu
def añadir_plato(plato: PlatoDTO): # el parametro plato es de tipo PlatoDTO, que es un objeto que contiene los datos del plato a agregar
    try:
        nuevo_id = menu_dao.agregar_plato(plato) # llama al metodo agregar_plato de la clase MenuDAO para agregar un plato a la base de datos
        return {"mensaje": "Plato agregado con éxito", "id": nuevo_id} # retorna un mensaje de éxito y el id del plato agregado
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) # si hay un error, retorna un error 500 con el detalle del error