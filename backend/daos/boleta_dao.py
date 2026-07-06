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

        #Armado de documento BSON
        documento_boleta = {
            "mesa_numero": pedido.mesa_numero,
            "fecha": datetime.now(),
            "estado": "pendiente",#Aun no se a pagado
            "items": [item.dict() for item in pedido.items], #Convierte cada item en un diccionario
            "total_boleta": total
           }
           #guardar la boleta en la coleccion boletas
        resultado = self.coleccion_boletas.insert_one(documento_boleta)

           #cambiar el estado de la mesa a ocupada
        self.coleccion_mesas.update_one(
            {"numero": pedido.mesa_numero},
            {"$set": {"estado":"ocupada"}}
        )

        #Retornar el Id de la boleta y total calculado
        return {
            "id_boleta": str(resultado.inserted_id),
           "total_boleta": total
        }