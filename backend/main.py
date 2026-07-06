from fastapi import FastAPI, HTTPException
from pymongo import MongoClient 
from dotenv import load_dotenv
import os

# IMPORTAMOS NUESTROS OBJETOS DESDE LAS OTRAS CARPETAS
from dtos.menu_dto import PlatoDTO
from daos.menu_dao import MenuDAO
from dtos.mesero_dto import PedidoDTO, EstadoMesaDTO
from daos.mesero_dao import MeseroDAO
from dtos.boleta_dto import NuevaBoletaDTO
from daos.boleta_dao import BoletaDAO

# con load_dotenv() cargamos las variables de entorno del archivo .env
load_dotenv() 
#crea el servidor de fastapi
app = FastAPI(title="SisGes API") 

# Conexión Global
MONGO_URI = os.getenv("MONGO_URI") 
cliente_mongo = MongoClient(MONGO_URI) 
db = cliente_mongo["resto_manager_db"]


# 2. INSTANCIAS DE LOS DAOs (Les pasamos la base de datos)
# al instanciar MenuDAO le pasamos la conexion a la base de datos para que pueda usarla en sus metodos
#el (db) es el parametro que le permite a la clase MenuDAO usar la conexion a la base de datos en sus metodos
menu_dao = MenuDAO(db) # Nueva instancia habilitada
mesero_dao = MeseroDAO(db) # Nueva instancia habilitada
boleta_dao = BoletaDAO(db) # Nueva instancia habilitada


# RUTAS DE ADMINISTRACIÓN (MENÚ)
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
    

# RUTAS DEL MESERO
# 1. Ver todas las mesas y sus estados
@app.get("/mesero/mesas")
def obtener_mesas():
    try:
        return mesero_dao.ver_mesas()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 2. Cambiar estado de una mesa manualmente (ej: cambiar a "reservada")
# Usamos PUT porque estamos actualizando un dato que ya existe
@app.put("/mesero/mesas/{numero_mesa}")
def cambiar_estado_mesa(numero_mesa: int, estado_data: EstadoMesaDTO):
    try:
        return mesero_dao.actualizar_estado_mesa(numero_mesa, estado_data.estado)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 3. Ver menú filtrado (solo lo que está disponible)
@app.get("/mesero/menu")
def ver_menu_mesero():
    try:
        return mesero_dao.ver_menu_disponible()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 4. Tomar el pedido (Guarda el pedido y cambia la mesa a "ocupada")
@app.post("/mesero/pedidos")
def crear_pedido(pedido: PedidoDTO):
    try:
        nuevo_id = mesero_dao.tomar_pedido(pedido)
        return {"mensaje": "Pedido registrado y mesa ocupada", "id_pedido": nuevo_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 5. Ver el total acumulado de una mesa
@app.get("/mesero/mesas/{numero_mesa}/total")
def obtener_total_mesa(numero_mesa: int):
    try:
        return mesero_dao.ver_total_mesa(numero_mesa)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 6. Generar la boleta (Cierra el pedido y cambia la mesa a "disponible")
@app.post("/mesero/mesas/{numero_mesa}/boleta")
def emitir_boleta(numero_mesa: int):
    try:
        return mesero_dao.generar_boleta(numero_mesa)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

