import pickle
from codigo.logica.tablero import*
from codigo.logica.configuracion import*

class Juego_Guardado:
    '''
    Recibe el tablero, el usuario, la PC y la bolsa de fichas y los almacena.
    Está construído para utilizar un botón para guardar y otro para cargar
    '''
    juego = []
    def __init__(self, ruta_guardado, tablero=None, jugador_user=None, atril=None, atril_pc=None, b_fichas=None, puntaje=None, puntaje_pc=None, tiempo_restante=None, pref=None, cant_cambiar=None):
        self.tablero = tablero
        self.jugador_user = jugador_user
        self.atril = atril
        self.bolsa_fichas = b_fichas
        self.atril_pc = atril_pc
        self.puntaje = puntaje
        self.tiempo_restante = tiempo_restante
        self.preferencias = pref
        self.cant_cambiar = cant_cambiar
        self.puntaje_pc = puntaje_pc
        self.ruta_guardado = ruta_guardado

    def getTablero (self):
        return self.tablero
    def getJugadorUser (self):
        return self.jugador_user
    def getAtril (self):
        return self.atril
    def getBolsaFichas (self):
        return self.bolsa_fichas
    def getPuntaje (self):
        return self.puntaje
    def getTiempoRestante(self):
        return self.tiempo_restante
    def getPreferencias(self):
        return self.preferencias
    def getCantCambiar(self):
        return self.cant_cambiar
    def getPuntajePC(self):
        return self.puntaje_pc
    def getRutaGuardado(self):
        return self.ruta_guardado
    def getAtrilPC(self):
        return self.atril_pc

    def crear_guardado(self):
        '''
        Cada vez que se lo invoca sobreescribe el archivo. Guarda una única partida
        '''
        fichero = open(f'{self.getRutaGuardado()}juego_guardado.pckl', 'wb')
        self.juego = [self.tablero, self.jugador_user, self.atril, self.bolsa_fichas, self.puntaje, self.tiempo_restante, self.preferencias, self.cant_cambiar, self.puntaje_pc, self.atril_pc]
        pickle.dump(self.juego, fichero)
        fichero.close()

    def cargar_guardado(self):
        try:
            fichero = open(f'{self.getRutaGuardado()}juego_guardado.pckl', 'rb')
            self.juego = pickle.load (fichero)
            fichero.close()
            self.tablero = self.juego[0]
            self.jugador_user = self.juego[1]
            self.atril = self.juego[2]
            self.bolsa_fichas = self.juego[3]
            self.puntaje = self.juego[4]
            self.tiempo_restante = self.juego[5]
            self.preferencias = self.juego[6]
            self.cant_cambiar = self.juego[7]
            self.puntaje_pc = self.juego[8]
            self.atril_pc = self.juego[9]
            return True
        except:
            print ('No hay partidas guardadas')
            return False


#A modo de prueba

# confi = nivel_dificil()
#
# configuracion = Preferencias(confi['filas'],confi['columnas'],confi['especiales'], confi['nivel'])
#
# unTablero = Tablero(configuracion)
#
# lista_fichas = [{'h': 4}, {'o': 5}, {'l': 9}, {'a': 3}]
# nuevas_fichas = [{'y': 4}, {'i': 5}]
# unTablero.insertarPalabra(lista_fichas, (2,4), "v")
# unTablero.insertarPalabra(nuevas_fichas, (2,1), "h")
#
# copiaTablero = unTablero
# jugador_user = 'Pepe'
# pc = 'Linux'
# bolsa_fichas = 'nada'
# juego = Juego_Guardado (copiaTablero,jugador_user,pc,bolsa_fichas, 66)
# #juego.crear_guardado()
# juego.mostrar()
