from logica.preferencias import Preferencias
from logica.configuracion import *

class Tablero ():
    def __init__(self, configuracion):
        self.__casilleros = self.__inicializarCasilleros(configuracion)

    def __inicializarCasilleros(self, configuracion):
        """Crea la matriz donde se insertarán las fichas a partir de una configuración.
        Si hay casilleros especiales, representados con un diccionario bajo
        el formato {'fila, columna': '*<color>'}, graba '*<color>' en la matriz,
        según las coordenadas de la clave."""
        matriz = []
        espacios_especiales = configuracion.getEspeciales()
        for f in range(0, configuracion.getFilas()):
            fila = []
            #Crea la fila, moviéndose entre columnas
            for c in range(0, configuracion.getColumnas()):
                #Si la ubicación actual está en el diccionario para espacios
                #especiales, toma el color y lo inserta en la matriz
                if (f'{f}, {c}' in espacios_especiales) or (f'{f},{c}' in espacios_especiales):
                    fila.append(espacios_especiales[f'{f}, {c}'])
                else:
                    fila.append('')
            matriz.append(fila)
        return matriz

    def getCasilleros(self):
        """Devuelve la matriz que representa el tablero"""
        return self.__casilleros

    def setCasilleros(self, casilleros):
        """Recibe una matriz y la asigna como tablero"""
        self.__casilleros = casilleros

    def insertarPalabra(self, fichas, posicion, sentido):
        """Recibe una lista de fichas en formato diccionario,
        una posicion en formato tupla (fila, columna) y un sentido en formato string
        ("h" o "v"). Luego, si hubiese lugar, inserta la palabra en el tablero
        siguiendo esas indicaciones.
        Además, retorna el puntaje para esa inserción."""
        casilleros = self.getCasilleros()
        #Fila
        f = posicion[0]
        #Columna
        c = posicion[1]
        puntaje = 0
        penitencia = 0
        if (sentido == 'h'):
            while (c < len(casilleros[posicion[0]])) and (c < (posicion[1] + len(fichas))):
                if (self.esFicha(f, c)):
                    break
                c += 1
            if (len(fichas) == c - posicion[1]):
                c = posicion[1]
                for fic in fichas:
                    casilleros[posicion[0]][c] = fic
                    c += 1
                self.setCasilleros(casilleros)
            else:
                puntaje = -1
        else:
            while (f < len(casilleros)) and (f < posicion[0] + len(fichas)):
                if (self.esFicha(f, c)):
                    break
                f += 1
            if (len(fichas) == f - posicion[0]):
                f = posicion[0]
                for fic in fichas:
                    casilleros[f][posicion[1]] = fic
                    f += 1
                self.setCasilleros(casilleros)
            else:
                puntaje = -1
        return puntaje

    def esFicha(self, f=-1, c=-1, ficha=None):
        """Determina si un objeto es o no una ficha, y retorna True o False
        dependiendo de ello.
        Si recibe fila y columna, evalúa lo que hay en esa posición.
        Si recibe una ficha, ignora las coordenadas y evalúa esa ficha en
        particular."""
        if (ficha == None):
            return isinstance(self.getCasilleros()[f][c], dict)
        else:
            return isinstance(ficha, dict)

    def imprimirCasilleros(self):
        """Imprime la matriz en formato string.
        Tiene propositos de testeo."""
        casilleros = self.getCasilleros()
        for fila in casilleros:
            for dato in fila:
                if (self.esFicha(ficha=dato)):
                    print(list(dato.keys())[0], end='  ')
                else:
                    if (dato == ''):
                        print('-', end='  ')
                    else:
                        print(dato[1:2], end='  ')
            print()

# confi = nivel_dificil()
#
# configuracion = Preferencias(confi['filas'],confi['columnas'],confi['especiales'])
#
# unTablero = Tablero(configuracion)
#
# lista_fichas = [{'h': 4}, {'o': 5}, {'l': 9}, {'a': 3}]
# nuevas_fichas = [{'a': 4}, {'g': 5}]
# unTablero.insertarPalabra(lista_fichas, (2,4), "v")
# unTablero.insertarPalabra(nuevas_fichas, (2,1), "h")
# unTablero.imprimirCasilleros()
