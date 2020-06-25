class Jugador():

    def __init__(self, nombre, puntaje = 0, dificultad ='facil', avatar = None):
        self.__nombre = nombre
        self.__puntuacion = puntaje
        self.__dificultad = dificultad
        self.__avatar = avatar


    def __str__(self):
        return 'Jugador: {} - Puntuación:  {}'.format(self.__nombre, self.__puntuacion)

    def infoJugador(self):
        return f"Nombre: {self.__nombre}\nPuntuación: {self.__puntuacion}\nDificultad: {self.__dificultad}"

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getPuntaje(self):
        return self.__puntuacion

    def setPuntaje(self, puntaje):
        self.__puntuacion = puntaje

    def getDificultad(self):
        return self.__dificultad

    def setDificultad(self, dificultad):
        self.__dificultad = dificultad

    def getAvatar(self):
        return self.__avatar