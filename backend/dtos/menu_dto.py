from pydantic import BaseModel

class PlatoDTO(BaseModel):
    nombre: str
    categoria: str #plato, bebida o postre
    precio: int
    disponible: bool = True