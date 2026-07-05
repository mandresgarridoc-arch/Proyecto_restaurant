from fastapi import FastAPI, HTTPException
from pymongo import MongoClient 
from dotenv import load_dotenv
import os

# IMPORTAMOS NUESTROS OBJETOS DESDE LAS OTRAS CARPETAS
from dtos.menu_dto import PlatoDTO
from daos.menu_dao import MenuDAO

# Inicialización
load_dotenv() 
app = FastAPI(title="SisGes API") 

# Conexión Global
MONGO_URI = os.getenv("MONGO_URI") 
cliente_mongo = MongoClient(MONGO_URI) 
db = cliente_mongo["resto_manager_db"]

# Instanciamos el DAO pasándole la base de datos configurada
menu_dao = MenuDAO(db)

@app.get("/admin/menu")
def ver_carta_completa():
    try:
        return menu_dao.obtener_platos()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/admin/menu")
def añadir_plato(plato: PlatoDTO):
    try:
        nuevo_id = menu_dao.agregar_plato(plato)
        return {"mensaje": "Plato agregado con éxito", "id": nuevo_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))