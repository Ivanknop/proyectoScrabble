import pickle
import os

class Jugador():

    def __init__(self,nombre,puntaje):
        self.nombre = nombre
        self.puntuacion = puntaje

    def __str__(self):
        return '{:^15} {:15} {:^15}'.format(self.nombre,' ', self.puntuacion)

class Puntuacion_Maxima():
    ruta_guardado = os.path.join("guardados", "puntuacion_maxima.pckl")
    MAXIMOS = 10

    def __init__ (self):
        self.puntajes = []
        self.cargar()

    def guardar(self):
        fichero = open(self.ruta_guardado, 'wb')
        pickle.dump(self.puntajes, fichero)
        fichero.close()

    def agregar(self,jug):
        '''
        Recibe un jugador y evalúa si su puntuación es mayor a las guardadas. Produce el desplazamiento y elimina a la posición 11
        '''
        self.puntajes.append(jug)
        self.puntajes.sort(key=lambda jugador: jugador.puntuacion,reverse=True)
        self.puntajes.pop()
        self.guardar()

    def cargar(self):
        try:
            fichero = open(self.ruta_guardado, 'rb')
            self.puntajes = pickle.load(fichero)
            fichero.close()
        except:
            print("El fichero no existe")
            

    def mostrar(self):
        if len(self.puntajes) == 0:
            print("No hay puntuaciones")
            return
        for j in self.puntajes:
            print(j)

    def ver_puntaje(self,pos):
        '''
        Devuelve una posición particular a partir de una posición específica
        '''
        return self.puntajes[pos]

    def _vaciar_puntajes (self):
        '''
            Es un método que solo se invoca desde la propia clase.
            Vacía la lista de puntuaciones
        '''
        self.puntajes = []
        for p in range (10):
            self.puntajes.append(Jugador('Vacío',0))
        self.puntajes = self.puntajes[0:self.MAXIMOS]
        self.guardar()

    def inicializar_puntuacion (self):
        '''
        Reinicializa las puntuaciones máximas
        '''
        #Siempre, antes de agregarse por primera vez un jugador, debe invocarse a "_vaciar_puntajes()"
        self._vaciar_puntajes()
        self.agregar(Jugador('Enzo',300))
        self.agregar(Jugador('Iván',300))
        self.agregar(Jugador('Diego',300))
        self.agregar(Jugador('Kakaroto',280))
        self.agregar(Jugador('Vegetta',250))
        self.agregar(Jugador('Quién',230))
        self.agregar(Jugador('Cómo',200))
        self.agregar(Jugador('Cuándo',150))
        self.agregar(Jugador('Qué',120))
        self.agregar(Jugador('Por qué',100))
        self.puntajes = self.puntajes[0:self.MAXIMOS]
        self.guardar()

    def borrar_puntuacion (self):
        '''
         Borra las puntuaciones máximas
        '''
        self._vaciar_puntajes()
        jug = Jugador ('###',0)
        for i in range(self.MAXIMOS):
            self.puntajes.append(jug)
        self.puntajes = self.puntajes[0:self.MAXIMOS]
        self.guardar()
