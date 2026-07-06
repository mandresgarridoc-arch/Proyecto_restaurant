from datetime import datetime
from dtos.boleta_dto import NuevaBoletaDTO

class BoletaDAO:
    def __init__(self, db):
       #aqui conectamos con las dos colecciones que vamos a usar, boletas y mesas 
       #para poder cambiar el estado de la mesa a disponible cuando se cierre la boleta
       self.coleccion_boletas = db["boletas"]
       self.coleccion_mesas = db["mesas"]

       def registrar_nuevo_pedido(self, pedido:NuevaBoletaDTO):
           #calcular el total del pedido 
           total = sum(item.cantidad * item.precio_unitario for item in pedido.items)

