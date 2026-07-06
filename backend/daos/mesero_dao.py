from bson import ObjectId
from dtos.mesero_dto import PedidoDTO
from datetime import datetime

#El mesero necesita interactuar con 3 colecciones distintas y aqui las dejamos como variables para que las use
class MeseroDAO:
    def __init__(self, db):
        self.db = db
        self.col_mesas = db["mesas"]
        self.col_pedidos = db["pedidos"]
        self.col_menu = db["menu"]

    
    # 1. GESTIÓN DE MESAS
   
    def ver_mesas(self):
        """Devuelve todas las mesas y sus estados"""
        cursor = self.col_mesas.find()
        lista = []
        for mesa in cursor:
            mesa["id"] = str(mesa["_id"])
            del mesa["_id"]
            lista.append(mesa)
        return lista

    def actualizar_estado_mesa(self, numero_mesa: int, nuevo_estado: str):
        """Permite cambiar a disponible, reservada u ocupada"""
        self.col_mesas.update_one(
            {"numero": numero_mesa}, #filtra la mesa por su numero exacto
            {"$set": {"estado": nuevo_estado}} #$set no borra nada solo actualiza el estado de la mesa
        )
        return {"mensaje": f"Mesa {numero_mesa} actualizada a {nuevo_estado}"}

   
    # 2. VER MENÚ DISPONIBLE
  
    def ver_menu_disponible(self):
        """Filtra y trae solo los platos y bebidas que están disponibles"""
        cursor = self.col_menu.find({"disponible": True}) #Con el true devuelve solo los platos que tenemos disponibles, el mesero no ve los platos agotados
        lista = []
        for item in cursor:
            item["id"] = str(item["_id"])
            del item["_id"]
            lista.append(item)
        return lista

    
    # 3. GESTIÓN DE PEDIDOS Y VENTAS
    
    def tomar_pedido(self, pedido: PedidoDTO):
        """Guarda el pedido y automáticamente marca la mesa como ocupada"""
        doc_pedido = pedido.dict() #dict convierte el objeto en un diccionario de python
        doc_pedido["fecha_hora"] = datetime.now() # Registramos la hora exacta
        
        # 1. Insertar el pedido en MongoDB
        resultado = self.col_pedidos.insert_one(doc_pedido)
        
        # 2. Cambiar el estado de la mesa a 'ocupada' automáticamente
        self.actualizar_estado_mesa(pedido.numero_mesa, "ocupada") #llama al metodo que hicimos mas arriba para poner la mesa como ocupada
        
        return str(resultado.inserted_id)

    def ver_total_mesa(self, numero_mesa: int):
        """Busca el pedido abierto de una mesa y muestra su total"""
        pedido = self.col_pedidos.find_one({"numero_mesa": numero_mesa, "estado": "abierto"})
        if pedido:
            return {"numero_mesa": numero_mesa, "total_acumulado": pedido["total"]}
        return {"mensaje": "La mesa no tiene pedidos abiertos."}

  
    # 4. GENERACIÓN DE BOLETA
  
    def generar_boleta(self, numero_mesa: int):
        """Cierra el pedido, genera el comprobante y libera la mesa"""
        pedido = self.col_pedidos.find_one({"numero_mesa": numero_mesa, "estado": "abierto"})
        
        if not pedido:
            return {"error": "No hay pedidos abiertos para generar boleta en esta mesa."}
        
        # 1. Cambiar el estado del pedido a 'cerrado'
        self.col_pedidos.update_one(
            {"_id": pedido["_id"]},
            {"$set": {"estado": "cerrado"}}
        )
        
        # 2. Liberar la mesa (cambiar a 'disponible')
        self.actualizar_estado_mesa(numero_mesa, "disponible")
        
        # 3. Retornar el formato de la boleta
        boleta = {
            "titulo": "BOLETA DE VENTA - RESTOMANAGER",
            "fecha": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "mesa": numero_mesa,
            "detalle_consumo": pedido["items"],
            "total_a_pagar": pedido["total"],
            "mensaje_despedida": "¡Gracias por su visita!"
        }
        return boleta