import PySimpleGUI as sg
from codigo.logica.puntuaciones_maximas import*
from codigo.interfaz.interfaz_puntaje import*
from codigo.interfaz.tema import *
from codigo.interfaz.interfaz_palabras import*


def ver_ganador (jug,pc,ven):
    '''
    Primero actualiza la pantalla con los puntajes de ambos jugadores. Después define el vencedor.
    '''
    ven['pje_jug'].update(value=jug)
    ven['pje_pc'].update(value=pc)
    if int(jug) > int(pc):
        ven['ganador'].update(value='GANASTE!!')
    else:
        ven['ganador'].update(value='QUÉ LÁSTIMA.. PERDISTE')

def terminar(nombre, punt_jug,punt_pc,pal_jug,pal_pc):
    contenido = [
        [sg.Text('TU PUNTAJE FINAL',size=(40,1),font=('Impact',14),justification='center',text_color=('#D09F61'),key='_jug')],
        [sg.Text(key='pje_jug',size=(50,1),justification='center',font=('Arial',50),background_color='Black',text_color='white')],
        [sg.Text('PUNTAJE DE LA PC',size=(40,1),font=('Impact',14),justification='center',text_color=('#D09F61'),key='_pc')],
        [sg.Text(key='pje_pc',size=(50,1),justification='center',font=('Arial',50),background_color='Black',text_color='white')],
        [sg.Text(key='ganador',size=(50,1),justification='center',font=('Arial',20),background_color='Black',text_color='white')],
        [sg.Button('Salir', font=('Arial', 16), size=(10, 1),button_color=('black', '#f75404'), key='salir') ]

        ]
    mi_tema()
    ven = sg.Window ('Ganador',layout=contenido,size= (400,400), no_titlebar=False)
    ven.finalize()

    while True:
        #Crea un puntaje, actualiza las puntuaciones máximas y abre la ventana de puntuaciones máximas
        puntaje = Puntuacion_Maxima()
        puntaje.agregar(Jugador(nombre,punt_jug))
        puntajes()        
        #Abre la ventana de las palabras utilizadas
        listado_palabras(pal_jug,pal_pc)
        #Abre la ventana donde se ve quién ganó
        ver_ganador (punt_jug,punt_pc,ven)
        event, values = ven.read()
        if event in (None,'salir'):
            break
    ven.close()
if __name__ == '__main__':
    terminar()