class Jugador():

    def __init__(self, nombre, puntaje = 0, dificultad ='facil', avatar = None):
        self.__nombre = nombre
        self.__puntuacion = puntaje
        self.__dificultad = dificultad
        self.__avatar = avatar


    def __str__(self):
        return 'Jugador: {} - Puntuación:  {}'.format(self.n__ombre, self.__puntuacion)

    def infoJugador(self):
        info = ( self.__nombre ,
                self.__puntuacion ,
                self.__dificultad ,
                self.__avatar ,
                    )

        return info

    def getNombre(self):
        return self.__nombre

    def getPuntos(self):
        return self.__puntuacion

    def getdificultad(self):
        return self.__dificultad

    def getAvatar(self):
        return self.__avatar