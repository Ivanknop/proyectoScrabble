class Preferencias():
    def __init__(self, cant_filas=5, cant_columnas=5, especiales={}):
        self.__filas = cant_filas
        self.__columnas = cant_columnas
        self.__especiales = especiales

    def getFilas(self):
        return self.__filas

    def getColumnas(self):
        return self.__columnas

    def getEspeciales(self):
        return self.__especiales

    def setFilas(self, filas):
        self.__filas = filas

    def setColumnas(self, columnas):
        self.__columnas = columnas
    
    def setEspeciales(self, especiales):
        self.__especiales = especiales
