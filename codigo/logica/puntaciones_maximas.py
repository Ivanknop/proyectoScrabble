import pickle

class Jugador():

    def __init__(self,nombre,puntaje):
        self.nombre = nombre
        self.puntuacion = puntaje
    
    def __str__(self):
        return '{} ({})'.format(self.nombre, self.puntuacion)

class Puntuacion_Maxima():
    puntajes = []    
    def __init__ (self):
        self.cargar()
    
    def guardar(self):
        fichero = open('puntuacion_maxima.pckl', 'wb')
        pickle.dump(self.puntajes, fichero)
        fichero.close()

    def agregar(self,jug):
        self.puntajes.append(jug)
        self.guardar()
        aux_jug = jug
        for i in range(len(self.puntajes)):
            if self.puntajes[i].puntuacion < aux_jug.puntuacion:
                    aux = self.puntajes[i]                    
                    self.puntajes[i]= aux_jug
                    aux_jug = aux 
    def cargar(self):
        fichero = open('puntuacion_maxima.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.puntajes = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            print("Se han cargado {} jugadores".format(len(self.puntajes)))

    def mostrar(self):
        if len(self.puntajes) == 0:
            print("No hay puntuaciones")
            return
        for j in self.puntajes:
            print(j)

puntuaciones = Puntuacion_Maxima()
puntuaciones.agregar(Jugador('Enzo','200'))
puntuaciones.agregar(Jugador('Iván','195'))
puntuaciones.agregar(Jugador('Diego','194'))
puntuaciones.agregar(Jugador('Kakaroto','150'))
puntuaciones.agregar(Jugador('Vegetta','149'))
puntuaciones.mostrar()