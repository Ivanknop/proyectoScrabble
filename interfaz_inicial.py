import PySimpleGUI as sg
import os
#luego acordate de poner bien esta ruta ucando lo sumes al proyecto
import codigo.interfaz.visorAvatar as va
from codigo.interfaz.visorAvatar import directorio
from codigo.logica.jugador import Jugador

ANCHO = 900  # solo de prueba
ALTO = 700  # solo de prueba

#asigno las rutas de las imagenes a usar
#la idea es tener un modulo que cargue la iniciar le programa, todas las imagenes necesarias
#para la aplaicacion. y usar excepciones por si no encunetra los archivos

#-----------------------------------------------

BML =  os.path.join('media','media_ii','botonlargo.png')
BM = os.path.join('media','media_ii','botonMadera.png')
LOGO = os.path.join('media','media_ii','logo.png')
#-----------------------------------------------


def nivel():
    ''' esta función devolvera el nivel elegido por el usuario
    se usa en el layout de nueva partida'''

    if ventana.FindElement('rFacil').Get() == True:
        n = "facil"
    elif ventana.FindElement('rMedio').Get() == True:
        n = 'medio'
    else:
        n = 'dificil'
    return n

def Jugar (avatar):

    '''esta funcion crea una instancia del objeto jugador y lo retorna'''
    if ventana.FindElement('apodo').Get() !=  '' :
        jugador= Jugador(nombre=value['apodo'],dificultad= nivel(),avatar =avatar)

    else:
        sg.popup_ok('Debe ingresar un Apodo')
        jugador = None

    return jugador


def mi_tema():
    sg.LOOK_AND_FEEL_TABLE['scrabble'] = {'BACKGROUND': '#4f280a', ##133d51',
                                            'TEXT': '#fff4c9',
                                            'INPUT': '#c7e78b',
                                            'TEXT_INPUT': '#000000',
                                            'SCROLL': '#c7e78b',
                                            'BUTTON': ('black', '#4f280a'),
                                            'PROGRESS': ('#01826B', '#D0D0D0'),
                                            'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                            }
    sg.theme('scrabble')


def actualizar_columnas(*columna):
    ''' esta función hara visible la columna que recibe com oparámetro
    y invisible el resto de las columnas
    esta función sirve para actualizar la interfaz principal segun la opción elegida'''
    '''elif e.Visible == False or e.Key == columna:
    print(e.Key, '  else')
    ventana.FindElement(e.Key).update(visible=True)'''
    for e in ventana.element_list():
        if e.Type == 'column':

            if e.Visible == False and e.Key in columna:

                ventana.FindElement(e.Key).update(visible=True)

            elif e.Key in columna:
                ventana.FindElement(e.Key).update(visible=True)


            else:
                ventana.FindElement(e.Key).update(visible=False)


def cargando():
    layout=[
        [sg.popup_animated(image_source='blue_blocks.gif', message="cargando...", alpha_channel=1,time_between_frames=2,no_titlebar=True)],
    ]
    return layout


def nueva_partida():
    global avatar

    layout = [
        [sg.Text('Apodo:', font=('Italic 24'),key='jugador')],

        [sg.InputText('',size=(20,20),font=('Italic 24'),background_color='blue',key='apodo')],
        [sg.Frame(
                  layout= [[sg.Radio('facil', "dificultad",font=('Italic 24'), default=True, size=(10,3), key='rFacil')],
                          [sg.Radio('Medio', "dificultad",font=('Italic 24'), default=False, size=(10,3), key='rMedio')],
                          [sg.Radio('Dificil', "dificultad",font=('Italic 24'), default=False, size=(10,3), key='rDificil')],],

                  title='Dificultad' ,title_color='black', relief=sg.RELIEF_SUNKEN,font=('Italic 24'),
                        element_justification='center',key='contenedor'),

         sg.Column(avatar.galAvatar(), visible=False,key='colAvatar')],


        [sg.Button('Jugar', size=(10, 2), key='_jugar_'),sg.Button('cancelar', size=(10, 2), key='_cancelar_')],
    ]
    return layout


def jugar_interfaz():
    layout = [
        [sg.Button('Nueva Partida',image_filename=BML,  border_width=0,font=('Italic 24'),size = (20,3), key='_nueva_')],
        [sg.Button('Cargar Partida',image_filename=BML,  border_width=0,font=('Italic 24'), size=(20,3), key='_cargar_')],
        [sg.Button('Volver',image_filename=BML,  border_width=0,font=('Italic 24'), size=(20,3), key='_volver_')],
    ]
    return layout

def inicio():
    layout = [[sg.Button(image_filename=BM, border_width=0,button_text='Ayuda', size=(200, 200), font=('Impact', 40), key='ayuda'),
               sg.Button(image_filename=BM, border_width=0, button_text='Jugar', size=(200, 200), font=('Impact', 40),key='jugar'),
               sg.Button(image_filename=BM,  border_width=0,button_text='Puntajes', size=(200, 200), font=('Impact', 30),key='puntajes')],
              [sg.Exit('Salir', button_color=('black','#f75404'),size=(8, 2), key='salir')]]
    return layout


def interfaz_principal (ALTO,ANCHO):

    colInicial = inicio()
    columnaCen2 = jugar_interfaz()
    columnaNueva = nueva_partida()
    layout = [
        [sg.Image(filename=LOGO)],
        [sg.Column(colInicial,justification='cener',element_justification='center',key= 'colInicial'),
         sg.Column(columnaCen2,visible=False,justification='cener',element_justification='center',key='colJugar2'),
         sg.Column(columnaNueva, visible=False,justification='cener',element_justification='center', key='colPartida'),
        ],


    ]

    return layout


avatarSelec = None
avatar=va.Visor(directorio)
mi_tema()
#layout = interfaz_principal(ALTO,ANCHO)

ventana = sg.Window('ScrabbleAr',size = (ANCHO,ALTO),resizable=False).Layout(interfaz_principal(ALTO,ANCHO))

ventana.Finalize()


ventana.FindElement('colInicial').update(visible=True)

while True:

    event, value = ventana.read()
    print(value)

    if event == 'salir':
        break
    elif event == 'jugar':

        actualizar_columnas('colJugar2')

    elif event == '_volver_':

        actualizar_columnas('colInicial')

    elif event == '_nueva_':
        actualizar_columnas('colPartida','colAvatar')
    elif event == '_cancelar_':
        actualizar_columnas('colJugar2')
    elif event == '_jugar_':
        jugador=Jugar(avatarSelec)
        if ventana.FindElement('apodo').Get()  :
            a = jugador.infoJugador()
            sg.popup_yes_no(a)
            print(a)
    elif event in ('<<<', '>>>'):

        avatarSelec=avatar.controles(event, ventana.FindElement('avatarVisor'))




