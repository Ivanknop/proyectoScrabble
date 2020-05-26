import PySimpleGUI as sg
from logica.tablero import *
from logica.configuracion import *
from logica.preferencias import Preferencias
from logica.atril import Atril
from logica.bolsa_fichas import *

class Dibujar():
    def __init__ (self, tablero, preferencias, atril):
        #Prepara y agrega a la columna izquierda todos los casilleros del tablero
        columna_izquierda = []
        numero_boton = 0
        for fila in tablero.getCasilleros():
            insercion = []
            for dato in fila:
                if (dato==''):
                    insercion.append(sg.Button(image_filename='azul.png', pad=(0,0), key=str(numero_boton), image_size=(29,31)))
                else:
                    insercion.append(sg.Button(image_filename=f'{dato[1:]}.png', pad=(0,0), key=str(numero_boton), image_size=(29,31)))
                numero_boton += 1
            columna_izquierda.append(insercion)

        fichas = []
        for i in range(0, atril.get_cant_fichas()):
            fichas.append(sg.Button(image_filename='unaFicha.png', image_size=(29,31), key=f'ficha {str(i)}'))
        fichas_oponente = []
        for i in range(0, atril.get_cant_fichas()):
            fichas_oponente.append(sg.Button(image_filename='unaFichaOponente.png', image_size=(29,31), key=f'ficha {str(i)}'))

        columna_derecha = [[sg.Image('scrabbleArLogo.png')],
                            [sg.Text(f'Nivel: {preferencias.getNivel()}', font=('Arial', 14))],
                            [sg.Text(f'Puntuación actual:', font=('Arial', 14))],
                            [sg.Text('Tiempo restante:', font=('Arial', 14))],
                            [sg.Text('_'*30)],
                            [sg.Text(' ---TUS FICHAS--- ', background_color='black', font=('Arial', 14), text_color='White')],
                            fichas,
                            [sg.Text('_'*30)],
                            [sg.Text(' ---FICHAS DEL OPONENTE--- ', background_color='black', font=('Arial', 14), text_color='White')],
                            fichas_oponente]

        #Crea la ventana y la muestra
        diseño = [[sg.Column(columna_izquierda), sg.Column(columna_derecha, element_justification='center', pad=(10, None))]]
        self.__interfaz = sg.Window('ScrabbleAR', diseño)
        self.__interfaz.Finalize()

confi = nivel_facil()
configuracion = Preferencias(confi['filas'],confi['columnas'],confi['especiales'], confi['nivel'])
unTablero = Tablero(configuracion)
bolsa_fichas = crear_bolsa(confi['cant_fichas'],confi['puntaje_ficha'])
FICHAS = 7
jugador = Atril (bolsa_fichas, FICHAS)
objeto_dibujo = Dibujar(unTablero, configuracion, jugador)
while True:
    input('ingrese algo')
    break
