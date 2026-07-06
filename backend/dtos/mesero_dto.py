from pydantic import BaseModel
from typing import List

# Sub-modelo: Representa un solo plato dentro de un pedido
class ItemPedidoDTO(BaseModel):
    nombre_plato: str
    cantidad: int
    precio_unitario: int

# Modelo Principal: Representa el pedido completo de una mesa
class PedidoDTO(BaseModel):
    numero_mesa: int
    items: List[ItemPedidoDTO] # Una lista de los platos pedidos
    total: int
    estado: str = "abierto" # Por defecto, al tomar el pedido está "abierto"

# Modelo para cambiar el estado de la mesa
class EstadoMesaDTO(BaseModel):
    estado: str # "disponible", "reservada", "ocupada"