from abc import ABC, abstractmethod

class EntidadVineria(ABC):

    @abstractmethod
    def __init__(self,id,nombre):
        self._id = id
        self._nombre = nombre

    def establecerNombre(self,nombre):
        self._nombre = nombre

    def obtenerId(self):
        return self._id

    def obtenerNombre(self):
        return self._nombre
    
    def __eq__(self, entidad):
        return self._id == entidad.obtenerId()