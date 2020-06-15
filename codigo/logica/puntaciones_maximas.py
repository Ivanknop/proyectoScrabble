import pickle

class Jugador():

    def __init__(self,nombre,puntaje):
        self.nombre = nombre
        self.puntuacion = puntaje
    
    def __str__(self):
        return 'Jugador: {} - Puntuación:  {}'.format(self.nombre, self.puntuacion)

class Puntuacion_Maxima():
    puntajes = []
    MAXIMOS = 10    
    def __init__ (self):
        self.cargar()
    
    def guardar(self):
        fichero = open('puntuacion_maxima.pckl', 'wb')
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
        fichero = open('puntuacion_maxima.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.puntajes = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()

    def mostrar(self):
        if len(self.puntajes) == 0:
            print("No hay puntuaciones")
            return
        for j in self.puntajes:
            print(j)
    
    def _vaciar_puntajes (self): 
        '''
            Es un método que solo se invoca desde la propia clase.
            Vacía la lista de puntuaciones
        '''
        self.puntajes = []

    def inicializar_puntuacion (self): 
        '''
        Reinicializa las puntuaciones máximas
        '''        
        self._vaciar_puntajes()
        self.puntajes.append(Jugador('Enzo',300))
        self.puntajes.append(Jugador('Iván',300))
        self.puntajes.append(Jugador('Diego',300))
        self.puntajes.append(Jugador('Kakaroto',280))
        self.puntajes.append(Jugador('Vegetta',250))
        self.puntajes.append(Jugador('Quién',230))
        self.puntajes.append(Jugador('Cómo',200))
        self.puntajes.append(Jugador('Cuándo',150))
        self.puntajes.append(Jugador('Qué',120))
        self.puntajes.append(Jugador('Por qué',100))
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
'''
Prueba

puntuaciones = Puntuacion_Maxima()
#puntuaciones.borrar_puntuacion()
puntuaciones.inicializar_puntuacion()
puntuaciones.mostrar()
'''
