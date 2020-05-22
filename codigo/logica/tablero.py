from preferencias import Preferencias

class Tablero ():
    def __init__(self, configuracion):
        self.__casilleros = self.__inicializarCasilleros(configuracion)

    def __inicializarCasilleros(self, configuracion):
        """Crea la matriz donde se insertarán las fichas a partir de una configuración.
        Si hay casilleros especiales, representados con un diccionario bajo
        el formato {'coordx, coordy': '*<color>'}, graba '*<color>' en la matriz,
        según las coordenadas de la clave."""
        matriz = []
        espacios_especiales = configuracion.getEspeciales()
        for x in range(0, configuracion.getFilas()):
            fila = []
            #Crea la fila, moviéndose entre columnas
            for y in range(0, configuracion.getColumnas()):
                #Si la coordenada actual está en el diccionario para espacios
                #especiales, toma el color y lo inserta en la matriz
                if (f'{x}, {y}' in espacios_especiales) or (f'{x},{y}' in espacios_especiales):
                    fila.append(espacios_especiales[f'{x}, {y}'])
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
        una posicion en formato tupla (x, y) y un sentido en formato string
        ("h" o "v"). Luego, si hubiese lugar, inserta la palabra en el tablero
        siguiendo esas indicaciones.
        Además, retorna el puntaje para esa inserción."""
        casilleros = self.getCasilleros()
        x = posicion[0]
        y = posicion[1]
        puntaje = 0
        penitencia = 0
        if (sentido == 'h'):
            while (y < len(casilleros[posicion[0]])) and (y < (posicion[1] + len(fichas))):
                if (self.esFicha(x, y)):
                    break
                y += 1
            if (len(fichas) == y - posicion[1]):
                y = posicion[1]
                for f in fichas:
                    casilleros[posicion[0]][y] = f
                    y += 1
                self.setCasilleros(casilleros)
        else:
            while (x < len(casilleros)) and (x < posicion[0] + len(fichas)):
                if (self.esFicha(x, y)):
                    break
                x += 1
            if (len(fichas) == x - posicion[0]):
                x = posicion[0]
                for f in fichas:
                    casilleros[x][posicion[1]] = f
                    x += 1
                self.setCasilleros(casilleros)
        return puntaje

    def esFicha(self, x=-1, y=-1, ficha=None):
        """Determina si un objeto es o no una ficha, y retorna True o False
        dependiendo de ello.
        Si recibe una coordenada, busca la ficha en el tablero.
        Si recibe una ficha, ignora las coordenadas y evalúa esa ficha en
        particular."""
        if (ficha == None):
            return isinstance(self.getCasilleros()[x][y], dict)
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
                        print(dato[0:2], end='  ')
            print()

configuracion = Preferencias(6, 8, {'4, 5': '*rojo'})
unTablero = Tablero(configuracion)

lista_fichas = [{'h': 4}, {'o': 5}, {'l': 9}, {'a': 3}]
nuevas_fichas = [{'a': 4}, {'g': 5}]
unTablero.insertarPalabra(lista_fichas, (2,4), "v")
unTablero.insertarPalabra(nuevas_fichas, (2,1), "h")
unTablero.imprimirCasilleros()
