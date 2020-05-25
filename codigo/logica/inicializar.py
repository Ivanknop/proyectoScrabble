#Escoge nivel e inicializa tablero y bolsa de fichas. Crea Atril 1
import PySimpleGUI as sg
from configuracion import *
from tablero import *
from preferencias import Preferencias
from bolsa_fichas import *
from atril import *

FICHAS = 7

ANCHO = 400 #solo de prueba
ALTO = 400  #solo de prueba

def configurar_juego (conf):
    '''
        Recibe el evento dificultad y configura el tablero y bolsas de fichas.
        Devuelve jugador, adversario, el tablero y la bolsa de fichas
    '''
    bolsa_fichas = crear_bolsa(conf['cant_fichas'],conf['puntaje_ficha'])
    jugador = Atril (bolsa_fichas, FICHAS)
    adversario = Atril (bolsa_fichas,FICHAS)        
    configuracion = Preferencias(conf['filas'],conf['columnas'],conf['especiales'])
    tablero = Tablero(configuracion)
    return jugador, adversario, tablero, bolsa_fichas


layout = [
    [sg.Text('Escoja el nivel de dificultad')],
    [sg.Button('Fácil',size = (40,2),font = ('Impact',20),key='facil')],
    [sg.Button ('Medio',size = (40,2),font = ('Impact',20),key='medio')],
    [sg.Button ('Difícil',size = (40,2),font = ('Impact',20),key='dificil')],
    [sg.Button ('Cómo jugar')],[sg.Button('Abir partida guardada')]
]
ventana = sg.Window('ScrabbleAr',layout = layout,size = (ANCHO,ALTO))

while True:
    event, values = ventana.read()
    if event == None:
        break
    elif event == 'facil':
        conf = nivel_facil()
        jugador, pc, tablero, b_fichas = configurar_juego (conf)
        tablero.imprimirCasilleros()
        print ('Atril Jugador:', jugador.ver_atril())
        print ('Atril PC: ',pc.ver_atril())
        print ('Nivel Fácil')
    elif event == 'medio':
        conf = nivel_medio()
        jugador, pc, tablero, b_fichas = configurar_juego (conf)
        tablero.imprimirCasilleros()
        print ('Atril Jugador:', jugador.ver_atril())
        print ('Atril PC: ',pc.ver_atril())
        print ('Nivel Medio')
    elif event == 'dificil':
        conf = nivel_dificil()
        jugador, pc, tablero, b_fichas = configurar_juego (conf)
        tablero.imprimirCasilleros()
        print ('Atril Jugador:', jugador.ver_atril())
        print ('Atril PC: ',pc.ver_atril())
        print ('Nivel Dificil')
ventana.close()
