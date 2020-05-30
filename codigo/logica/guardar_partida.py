import pickle 
from tablero import*
from configuracion import*

class Juego_Guardado:
    '''
    Recibe el tablero, el usuario, la PC y la bolsa de fichas y los almacena.
    Está construído para utilizar un botón para guardar y otro para cargar
    '''
    juego = []
    def __init__(self, tablero, jugador, pc,b_fichas):
        self.tablero = tablero
        self.jugador = jugador
        self.pc = pc
        self.bolsa_fichas = b_fichas
        #Los gets son de prueba
#    def getJugador (self):
#        return self.jugador
#    def getPc (self):
#        return self.pc
#    def getBolsaFichas (self):
#        return self.bolsa_fichas
#    def getTablero (self):
#        self.tablero.imprimirCasilleros()
    def crear_guardado(self):
        '''
        Cada vez que se lo invoca sobreescribe el archivo. Guarda una única partida
        '''
        fichero = open('juego_guardado.pckl', 'wb')
        self.juego = [self.tablero,self.jugador,self.pc,self.bolsa_fichas]
        pickle.dump(juego, fichero)
        fichero.close()
    def mostrar(self): 
        fichero = open('juego_guardado.pckl', 'rb')
        fichero.seek(0)
        try:
           self.juego = pickle.load (fichero)
        except:
            print ('No hay partidas guardadas')
        finally:
            fichero.close()
        print(juego.jugador)
        print (juego.pc)
        print (juego.bolsa_fichas)
        juego.tablero.imprimirCasilleros()
#A modo de prueba
'''
confi = nivel_dificil()
#
configuracion = Preferencias(confi['filas'],confi['columnas'],confi['especiales'])
#
unTablero = Tablero(configuracion)
#
lista_fichas = [{'h': 4}, {'o': 5}, {'l': 9}, {'a': 3}]
nuevas_fichas = [{'y': 4}, {'i': 5}]
unTablero.insertarPalabra(lista_fichas, (2,4), "v")
unTablero.insertarPalabra(nuevas_fichas, (2,1), "h")

copiaTablero = unTablero
jugador = 'Pepe'
pc = 'Linux'
bolsa_fichas = 'nada'
juego = Juego_Guardado (copiaTablero,jugador,pc,bolsa_fichas)
juego.mostrar()
'''