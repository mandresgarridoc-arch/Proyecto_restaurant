from bson import ObjectId

#importamos el DTO para saber que tipo 
# y de donde vamos a recibir y enviar datos
from dtos.menu_dto import PlatoDTO

class MenuDAO:
    def __init__(self, db):
        self.db = db #Se llama a si misma con un self.db para poder usarla en todos los metodos de la clase
        self.coleccion = db["menu"] #Se llama a la coleccion de menu de la base de datos
        #self significa que es un metodo propio de la clase, y no un metodo externo que se llama desde otro lado
      
    def obtener_platos(self):
        #llamar al cursor de mongo para traer todos los platos de la coleccion menu
        cursor = self.coleccion.find()
        #convierte el cursor en una lista vacia
        lista = []
        for plato in cursor:
            plato["id"] = str(plato["_id"]) #convierte el id de mongo en un string para que el navegador lo pueda leer
            del plato["_id"] #elimina el campo _id original para que no se duplique
            lista.append(plato) #agrega el plato a la lista
        return lista #retorna la lista de platos

    def agregar_plato(self, plato: PlatoDTO):
           doc_plato = plato.dict() #convierte el DTO en un diccionario para poder guardarlo en mongo
           resultado = self.coleccion.insert_one(doc_plato) #inserta el plato en la coleccion menu
           return str (resultado.inserted_id) #retorna el id del plato agregado