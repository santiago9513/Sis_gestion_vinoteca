import json
import vinoteca
from modelos.entidadvineria import EntidadVineria

class Bodega(EntidadVineria):

    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def obtenerVinos(self):
        vinosTodos = vinoteca.Vinoteca.obtenerVinos()
        vinos = []
        for vino in vinosTodos:
            if vino.obtenerBodega() == self:
                vinos.append(vino)
        return vinos

    def obtenerCepas(self):
        vinos = self.obtenerVinos()
        cepas = []
        for vino in vinos:
            for cepa in vino.obtenerCepas():
                if not cepa in cepas:
                    cepas.append(cepa)
        return cepas

    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(lambda a: a.obtenerNombre(), vinos)
        return list(vinosMapa)
