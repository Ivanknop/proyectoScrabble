from configuracion import *
from tablero import *
from preferencias import Preferencias
from bolsa_fichas import *
from atril import *

FICHAS = 7
nivel = str(input('Ingrese nivel de dificultad (1) Fácil, 2) Medio, 3) Difícil : \n '))
if nivel == '1':
    conf = nivel_facil()
    bolsa_fichas = crear_bolsa(conf['cant_fichas'],conf['puntaje_ficha'])
    jugador = Atril (bolsa_fichas, FICHAS)
    print ('Nivel Fácil')
    configuracion = Preferencias(conf['filas'],conf['columnas'],conf['especiales'])
    tablero = Tablero(configuracion)
    tablero.imprimirCasilleros()
    print ('Atril:', jugador.ver_atril())
elif nivel == '2':
    conf = nivel_medio()
    bolsa_fichas = crear_bolsa(conf['cant_fichas'],conf['puntaje_ficha'])
    jugador = Atril (bolsa_fichas, FICHAS)
    print ('Nivel Medio')
    configuracion = Preferencias(conf['filas'],conf['columnas'],conf['especiales'])
    tablero = Tablero(configuracion)
    tablero.imprimirCasilleros()
    print ('Atril:', jugador.ver_atril())
elif nivel == '3':
    conf = nivel_dificil()
    bolsa_fichas = crear_bolsa(conf['cant_fichas'],conf['puntaje_ficha'])
    jugador = Atril (bolsa_fichas, FICHAS)
    print ('Nivel Difícil')
    configuracion = Preferencias(conf['filas'],conf['columnas'],conf['especiales'])
    tablero = Tablero(configuracion)
    tablero.imprimirCasilleros()
    print ('Atril:', jugador.ver_atril())
