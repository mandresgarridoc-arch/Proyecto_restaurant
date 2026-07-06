#Con List indico que un pedido trae una lista de objetos
from pydantic import BaseModel
from typing import List

#DEfinir como viene cada plato individual en el pedido
class ItemPedidoDTO(BaseModel):
    producto_id: str
    nombre: str
    cantidad: int
    precio_unitario: int

#Definir como viene el pedido desde React
class NuevBoletaDTO(BaseModel):
    mesa_numero: int
    items:List[ItemPedidoDTO] #La lista de platos que trae el pedido