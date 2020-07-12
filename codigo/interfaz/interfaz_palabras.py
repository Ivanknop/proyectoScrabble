import PySimpleGUI as sg
#from tema import *
from codigo.interfaz.tema import *


def listado_palabras (jugador,pc):
        
    def listar (jugador,pc):
        j_pal = []
        j_pun =[]
        for p in range (len(jugador)):
            j_pal = j_pal + list(jugador[p].keys())
            j_pun = j_pun + list(jugador[p].values())
        pal_jug = ''
        for pal in range(len(jugador)):
            pal_jug = pal_jug + str(j_pal[pal].upper()) + ': ' + str(j_pun[pal]) + ' | '
        pc_pal = []
        pc_pun = []
        pal_pc = ''
        for p in range (len(pc)):
            pc_pal = pc_pal + list(pc[p].keys())
            pc_pun = pc_pun + list(pc[p].values())        
        for pal in range(len(pc)):
            pal_pc = pal_pc + str(pc_pal[pal].upper()) + ': ' + str(pc_pun[pal]) + ' | '
        ven['pal_jugador'].update(value=pal_jug)
        ven['pal_pc'].update(value=pal_pc)


    contenido = [
        [sg.Text('Palabras utilizadas por el Jugador',size=(40,1),font=('Impact',14),justification='center',text_color=('black'),key='_jug')],
        [sg.Text(key='pal_jugador',size=(200,10),justification='center',font=('Arial',16),background_color='Black',text_color='white')],
        [sg.Text('Palabras utilizadas por la PC',size=(40,1),font=('Impact',14),justification='center',text_color=('black'),key='_pc')],
        [sg.Text(key='pal_pc',size=(200,10),justification='center',font=('Arial',16),background_color='Black',text_color='white')],
        [sg.Button('salir', font=('Arial', 16), size=(10, 3),button_color=('black', '#f75404'), key='salir') ]

        ]
    mi_tema()
    ven = sg.Window ('Listado de Palabras',layout=contenido,size= (400,600), no_titlebar=False)
    ven.finalize()

    while True:
        
        listar (jugador,pc)
        event, values = ven.read()
        if event in ( None,'salir'):
            break
    ven.close()


#j = [{'hola':'2'},{'chau':'5'},{'lala':'36'}]
#p = [{'hola':'22'},{'cdsdshau':'5'},{'lala':'36'},{'perro':'100'}]


if __name__ == '__main__':
    listado_palabras()