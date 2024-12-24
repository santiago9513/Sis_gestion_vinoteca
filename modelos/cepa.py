import json
import vinoteca
from modelos.entidadvineria import EntidadVineria



class Cepa(EntidadVineria):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)
    
    def obtenerVinos(self):
        vinosTodos = vinoteca.Vinoteca.obtenerVinos()
        vinos = []
        for vino in vinosTodos:
            if self in vino.obtenerCepas():
                vinos.append(vino)
        return vinos

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(
            lambda a: a.obtenerNombre()
            + " ("
            + a.obtenerBodega().obtenerNombre()
            + ")",
            vinos,
        )
        return list(vinosMapa)
