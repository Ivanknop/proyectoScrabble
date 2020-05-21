from preferencias import Preferencias

class Tablero ():
    def __init__(self, configuracion):
        self.__casilleros = self.__inicializarCasilleros(configuracion)

    def __inicializarCasilleros(self, configuracion):
        matriz = []
        espacios_especiales = configuracion.getEspeciales()
        for x in range(0, configuracion.getFilas()):
            fila = []
            for y in range(0, configuracion.getColumnas()):
                if (f'{x}, {y}' in espacios_especiales) or (f'{x},{y}' in espacios_especiales):
                    fila.append(espacios_especiales[f'{x}, {y}'])
                else:
                    fila.append('')
            matriz.append(fila)
        return matriz

    def getCasilleros(self):
        return self.__casilleros

    def setCasilleros(self, casilleros):
        self.__casilleros = casilleros

    def insertarPalabra(self, palabra, posicion, sentido):
        """Recibe una palabra en formato string, una posicion en formato tupla
        (x, y) y un sentido en formato string ("h" o "v").
        Luego, si hubiese lugar, inserta la palabra en el tablero siguiendo
        esas indicaciones.
        Además, retorna el puntaje para esa inserción."""
        lista_caracteres = [caracter for caracter in palabra]
        casilleros = self.getCasilleros()
        x = posicion[0]
        y = posicion[1]
        puntaje = 0
        penitencia = 0
        if (sentido == 'h'):
            while (y < len(casilleros[posicion[0]])) and (y < (posicion[1] + len(palabra))):
                if (casilleros[x][y] == '') or (casilleros[x][y][0] == '*'):
                    y += 1
            if (len(palabra) == y - posicion[1]):
                y = posicion[1]
                for caracter in palabra:
                    casilleros[posicion[0]][y] = caracter
                    y += 1
                self.setCasilleros(casilleros)
        else:
            pass

        return puntaje


    def verCasilleros(self):
        for fila in self.getCasilleros():
            print(fila)

configuracion = Preferencias(6, 8, {'4, 5': '*rojo'})
unTablero = Tablero(configuracion)
puntaje = unTablero.insertarPalabra("hola", (4,4), "h")
unTablero.verCasilleros()


matriz = unTablero.getCasilleros()[4][4]
print(matriz)
