import PySimpleGUI as sg
from puntuaciones_maximas import*


def textos (pos):
    return listados[pos].Text

def actualizar_puntaje (puntaje):
    listado_puntos =''
    for p in range(len(puntaje.puntajes)): 
        listado_puntos = listado_puntos + str(puntaje.puntajes[p]) + '\n'
        ventana['puntos'].update(value=listado_puntos)

def blanquear (puntaje):
    puntaje._vaciar_puntajes()
    puntaje.guardar()
    actualizar_puntaje(puntaje)

contenido = [
    [sg.Text('Puntuaciones máximas',size=(20,1),font=('Impact',18),text_color=('black'),key='_puntos')],
    [sg.Text(key='puntos',size=(20,10),justification='center',background_color='Black',text_color='white')],
    [sg.Button('Borrar puntuación',font=('Arial',8),size=(20,3),key='blanquear'),    
    sg.Button('Reestablecer puntuación',font=('Arial',8),size=(20,3),key='reestablecer')]
]
def mostrar_ventana ():
    ventana = sg.Window ('Puntaje Máximo',layout=contenido,size= (400,400))
    ventana.finalize()
    while True:    
        puntuaciones = Puntuacion_Maxima()
        actualizar_puntaje(puntuaciones)
        event, values = ventana.read()
        if event == None:
            break
        elif event == 'blanquear':
            puntuaciones._vaciar_puntajes()
            actualizar_puntaje(puntuaciones)
        elif event == 'reestablecer':
            puntuaciones.inicializar_puntuacion()
            actualizar_puntaje(puntuaciones)
    ventana.close()