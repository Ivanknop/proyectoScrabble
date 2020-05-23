import PySimpleGUI as sg
from logica.tablero import *
from logica.configuracion import *
from logica.preferencias import Preferencias

class Dibujar():
    def __init__ (self, tablero):
        tableroGUI = []
        numero_boton = 0
        for fila in tablero.getCasilleros():
            insercion = []
            for dato in fila:
                if (dato==''):
                    insercion.append(sg.Button(image_filename='azul.png', pad=(0,0), key=str(numero_boton), image_size=(29,31)))
                else:
                    insercion.append(sg.Button(image_filename=f'{dato[1:]}.png', pad=(0,0), key=str(numero_boton), image_size=(29,31)))
                numero_boton += 1
            tableroGUI.append(insercion)
        self.__interfaz = sg.Window('ScrabbleAR', tableroGUI)
        self.__interfaz.Finalize()

confi = nivel_facil()
configuracion = Preferencias(confi['filas'],confi['columnas'],confi['especiales'])
unTablero = Tablero(configuracion)
objeto_dibujo = Dibujar(unTablero)
while True:
    input('ingrese algo')
    break
