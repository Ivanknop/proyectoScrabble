import PySimpleGUI as sg
from codigo.logica.puntuaciones_maximas import *
from codigo.interfaz.tema import *
import os
def actualizar_puntaje (puntaje,ventana):
    listado_puntos =''
    for p in range(len(puntaje.puntajes)):
        listado_puntos = listado_puntos + str(puntaje.puntajes[p]) + '\n'
        ventana['puntos'].update(value=listado_puntos)

def blanquear (puntaje):
    puntaje._vaciar_puntajes()
    puntaje.guardar()
    actualizar_puntaje(puntaje)

def puntajes():

    imgPuntos = os.path.join('media', 'puntuaciones2.png')
    contenido = [
        #[sg.Text('Puntuaciones máximas',size=(20,1),font=('Impact',18),text_color=('black'),key='_puntos')],
        [sg.Image(filename=imgPuntos, )],
        [sg.Text(key='puntos',size=(200,10),justification='center',font=('Impact',16),background_color='#afad71',text_color='Black')],
        [sg.Button('Borrar puntuación',font=('Arial',16),size=(10,3),button_color=('black', '#f75404'),key='blanquear'),
        sg.Button('Reestablecer puntuación',font=('Arial',16),size=(10,3),button_color=('black', '#f75404'),key='reestablecer'),
         sg.Button('volver', font=('Arial', 16), size=(14, 3),button_color=('black', '#f75404'), key='volver') ]

        ]
    mi_tema()
    ventana = sg.Window ('Puntaje Máximo',layout=contenido,size= (420,500),element_justification='center', no_titlebar=True,grab_anywhere=True, keep_on_top=True)
    ventana.finalize()

    puntuaciones = Puntuacion_Maxima()
    while True:
        actualizar_puntaje(puntuaciones,ventana)
        event, values = ventana.read()
        if event in ( None,'volver'):
            break
        elif event == 'blanquear':
            decision = sg.popup_yes_no('Realmente desea borrar los puntajes?',background_color='#ece6eb',text_color='black', button_color=('black','#f75404'),font=('Arial',14), no_titlebar=True, keep_on_top=True)
            if decision == 'Yes':
                puntuaciones._vaciar_puntajes()
                actualizar_puntaje(puntuaciones,ventana)
        elif event == 'reestablecer':
            decision = sg.popup_yes_no('Realmente desea reestablecer los puntajes?',background_color='#ece6eb',text_color='black', button_color=('black','#f75404'),font=('Arial',14), no_titlebar=True, keep_on_top=True)
            if decision == 'Yes':
                puntuaciones.inicializar_puntuacion()
                actualizar_puntaje(puntuaciones,ventana)
    ventana.close()


if __name__ == '__main__':
    puntajes()
