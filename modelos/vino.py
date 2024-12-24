import json
import vinoteca
from modelos.entidadvineria import EntidadVineria

class Vino(EntidadVineria):

    def __init__(self, id, nombre, bodega:(str), cepas:list[str], partidas:list[int]):
        super().__init__(id, nombre)
        self.__bodega = bodega
        self.__cepas = cepas
        self.__partidas = partidas

    def establecerBodega(self, bodega:(str)):
        self.__bodega = bodega
    def establecerCepas(self, cepas:list[str]):
        self.__cepas = cepas
    def establecerPartidas(self, partidas:list[int]):
        self.__partidas = partidas

    def obtenerBodega(self):
        bodega = vinoteca.Vinoteca.buscarBodega(self.__bodega)
        return bodega
    
    def obtenerCepas(self):
        cepasTodas = vinoteca.Vinoteca.obtenerCepas()
        cepas = []
        for cepa in cepasTodas:
            for cepaVino in self.__cepas:
                if cepaVino == cepa.obtenerId():
                    cepas.append(cepa)
        return cepas
    
    def obtenerPartidas(self):
        return self.__partidas
    

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self.__partidas,
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self.__partidas,
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)
