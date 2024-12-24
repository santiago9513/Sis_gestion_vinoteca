# librerias
import os
import json

# modelos
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino


class Vinoteca:

    __archivoDeDatos = "vinoteca.json"
    __bodegas = []
    __cepas = []
    __vinos = []

    def inicializar():
        datos = Vinoteca.__parsearArchivoDeDatos()
        Vinoteca.__convertirJsonAListas(datos)

    def obtenerBodegas(orden=None, reverso=False):
        lista = Vinoteca.__bodegas
        if isinstance(orden, str):
            if orden == "nombre":
                lista = sorted(lista, key = lambda bodega: bodega.obtenerNombre(), reverse = reverso)
            elif orden == "vinos":
                lista = sorted(lista, key = lambda bodega: len(bodega.obtenerVinos()), reverse = reverso)
        return lista

    def obtenerCepas(orden=None, reverso=False):
        lista = Vinoteca.__cepas
        if isinstance(orden, str):
            if orden == "nombre":
                lista = sorted(lista, key = lambda cepa: cepa.obtenerNombre(), reverse = reverso)
        return lista

    def obtenerVinos(anio=None, orden=None, reverso=False):
        lista = Vinoteca.__vinos
        if isinstance(anio, int):
            listaAux = []
            for vino in lista:
                if anio in vino.obtenerPartidas():
                    listaAux.append(vino)
            lista = listaAux
        if isinstance(orden, str):
            if orden == "nombre":
                lista = sorted(lista, key = lambda vino: vino.obtenerNombre(), reverse = reverso)
            elif orden == "bodega":
                lista = sorted(lista, key = lambda vino: vino.obtenerBodega().obtenerNombre(), reverse = reverso)     
            elif orden == "cepas":
                lista = sorted(lista, key = lambda vino: len(vino.obtenerCepas()), reverse = reverso)
        return lista

    def buscarBodega(id):
        for bodega in Vinoteca.__bodegas:
            if bodega.obtenerId() == id:
                return bodega
        return None

    def buscarCepa(id):
        for cepa in Vinoteca.__cepas:
            if cepa.obtenerId() == id:
                return cepa
        return None

    def buscarVino(id):
        for vino in Vinoteca.__vinos:
            if vino.obtenerId() == id:
                return vino
        return None

    def __parsearArchivoDeDatos():
        with open(Vinoteca.__archivoDeDatos,'r', encoding='utf-8') as archivo:
            dic = json.loads(archivo.read())
        return dic

    def __convertirJsonAListas(lista):
        for bodega in lista['bodegas']:
            Vinoteca.__bodegas.append(Bodega(bodega['id'],bodega['nombre']))
        for cepa in lista['cepas']:
            Vinoteca.__cepas.append(Cepa(cepa['id'],cepa['nombre']))
        for vino in lista['vinos']:
            Vinoteca.__vinos.append(Vino(vino['id'],vino['nombre'],vino['bodega'],vino['cepas'],vino['partidas']))
