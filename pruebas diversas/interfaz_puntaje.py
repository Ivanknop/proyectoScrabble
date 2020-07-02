import PySimpleGUI as sg
from codigo.logica.puntaciones_maximas import *


def textos (pos):
    return listados[pos].Text

def actualizar_puntaje (puntaje):
    listado_puntos =[]
    for p in range(len(puntaje.puntajes)):    
        venPuntos[str(p)].update(value=puntaje.ver_puntaje(p))

def blanquear (puntaje):
    puntaje._vaciar_puntajes()
    puntaje.guardar()
    actualizar_puntaje(puntaje)

def puntajes():
    contenido = [
        [sg.Text('Puntuaciones máximas',size=(20,1),font=('Impact',18),text_color=('black'),key='_puntos')],
        [sg.Text(key='0',size=(30,1),background_color='white',text_color='black' )],
        [sg.Text(key='1',size=(30,1),background_color='black',text_color='white')],
        [sg.Text(key='2',size=(30,1),background_color='white',text_color='black')],
        [sg.Text(key='3',size=(30,1),background_color='black',text_color='white')],
        [sg.Text(key='4',size=(30,1),background_color='white',text_color='black')],
        [sg.Text(key='5',size=(30,1),background_color='black',text_color='white')],
        [sg.Text(key='6',size=(30,1),background_color='white',text_color='black')],
        [sg.Text(key='7',size=(30,1),background_color='black',text_color='white')],
        [sg.Text(key='8',size=(30,1),background_color='white',text_color='black')],
        [sg.Text(key='9',size=(30,1),background_color='black',text_color='white')],
        [sg.Button('Borrar puntuación',font=('Arial',8),size=(20,3),key='blanquear'),
        sg.Button('Reestablecer puntuación',font=('Arial',8),size=(20,3),key='reestablecer')]
    ]

    venPuntos = sg.Window ('Puntaje Máximo',layout=contenido,size= (400,400))
    venPuntos.Finalize()
    while True:
        puntuaciones = Puntuacion_Maxima()
        actualizar_puntaje(puntuaciones)
        event, values = venPuntos.read()
        if event == None:
            break
        elif event == 'blanquear':
            puntuaciones._vaciar_puntajes()
            actualizar_puntaje(puntuaciones)
        elif event == 'reestablecer':
            puntuaciones.inicializar_puntuacion()
            actualizar_puntaje(puntuaciones)
    venPuntos.close()