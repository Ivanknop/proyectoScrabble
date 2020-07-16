import PySimpleGUI as sg
import os
from codigo.interfaz.tema import mi_tema

def general(dirAyuda):
    sg.theme_text_element_background_color('#4f280a')
    sg.theme_element_background_color('#4f280a')
    col = [[sg.Image(filename=f'{dirAyuda}ba.png'),sg.Text(' Muestra la Ayuda',font=('Arial, 18'),text_color='white')],
           [sg.Image(filename=f'{dirAyuda}bj.png'),sg.Text(' Comenzar a jugar',font=('Arial, 18'),text_color='white')],
           [sg.Image(filename=f'{dirAyuda}bp.png'), sg.Text('Muestra la Tabla de Puntajes', font=('Arial, 18'), text_color='white')],
           [sg.Image(filename=f'{dirAyuda}bnueva.png'), sg.Text('Iniciar una Nueva partida', font=('Arial, 18'), text_color='white')],
           [sg.Image(filename=f'{dirAyuda}bcargar.png'), sg.Text('Carga la ultima partida guardada. Si existe', font=('Arial, 18'), text_color='white')],
           [sg.Image(filename=f'{dirAyuda}bvolver.png'), sg.Text('Vuelve al Menu principal', font=('Arial, 18'), text_color='white')],
           [sg.Image(filename=f'{dirAyuda}nueva.png'), sg.Text(''
                                                      'En esta ventana usted podrá configurar \nlos datos para'
                                                      'la nueva partida\n'
                                                      'el apodo debe tener entre 3 y 10 caractere, sin caracteres especiales\n'
                                                      'Debe indicar una dificultad (or defecto se inicia en modo Fácil)\n'
                                                      'al momento de precionar en Jugar se le mostrará un ventana de ocnfirmación\n'
                                                      'en todo momento usted podrá cancelar esta acción\n',auto_size_text=True, font=('Arial, 14'), text_color='white')],
    ]


    layout = [sg.Column(col,scrollable=True,background_color='#4f280a',vertical_scroll_only=True,size=(700,470))]


    return layout

def juego(dirAyuda):
    col = [
        [sg.Image(filename=f'{dirAyuda}ba.png'), sg.Text(' Muestra la Ayuda', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}bj.png'), sg.Text(' Comenzar a jugar', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}bp.png'),
         sg.Text('Muestra la Tabla de Puntajes', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}bnueva.png'),
         sg.Text('Iniciar una Nueva partida', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}bcargar.png'),
         sg.Text('Carga la ultima partida guardada. Si existe', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}bvolver.png'),
         sg.Text('Vuelve al Menu principal', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}nueva.png'), sg.Text('',
                                                            font=('Arial, 18'), text_color='white')],
        ]

    layout = [sg.Column(col,scrollable=True,background_color='#4f280a', vertical_scroll_only=True,size=(700,470))]

    return layout

def iconCas(dirAyuda):
    col = [
        [sg.Image(filename=f'{dirAyuda}orientacionG.png'), sg.Text('Casillero seleccionado para insertar palabra', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}orientacionDrerechaG.png'), sg.Text('insertar horizontalmente', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}orientacionAbajoG.png'),
         sg.Text('insertar verticalmente', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}sumaG.png'),
         sg.Text('Incrementa 5 puntos el valor total de la palabra', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}menosG.png'),
         sg.Text('Resta 5 puntos al valor total de la palabra', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}multGi.png'),
         sg.Text('Duplica el valor de la palabra', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}divG.png'),
         sg.Text('Divide a la mitad el valor de la palabra', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ceroG.png'),
         sg.Text('Anula el valor de la palabra', font=('Arial, 18'), text_color='white')],

        ]

    layout = [sg.Column(col,scrollable=True,background_color='#4f280a', vertical_scroll_only=True,size=(700,470))]

    return layout

def otros(dirAyuda):
    col = [
        [sg.Image(filename=f'{dirAyuda}ba.png'), sg.Text(' Muestra la Ayuda', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}bj.png'), sg.Text(' Comenzar a jugar', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}bp.png'),
         sg.Text('Muestra la Tabla de Puntajes', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}bnueva.png'),
         sg.Text('Iniciar una Nueva partida', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}bcargar.png'),
         sg.Text('Carga la ultima partida guardada. Si existe', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}bvolver.png'),
         sg.Text('Vuelve al Menu principal', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}nueva.png'), sg.Text('',
                                                            font=('Arial, 18'), text_color='white')],
        ]

    layout = [sg.Column(col,scrollable=True,background_color='#4f280a', vertical_scroll_only=True,size=(700,470))]

    return layout

def ayuda() :
    '''esta función  es la encargada de motrar la interfaz
    que brinda ayuda a los/as Jugadores/as. Da información de cómo se juega
    detalle información de ventanas y popUps que utiliza  la aplicación '''

    dirAyuda = os.path.join('media','ayuda','')

    tabGeneral = [general(dirAyuda)]
    tabJuego = [juego(dirAyuda)]
    tabIconCas = [iconCas(dirAyuda)]
    tabOtros = [otros(dirAyuda)]
    # Agregar solapa o boton que te de un poco de info del proyecto, un link a Git y que diga que en el informe ocmpleto hay mas info


    layout = [[sg.TabGroup([[sg.Tab('General', tabGeneral,background_color='#4f280a',  key='pGeneral'),
                          sg.Tab('Instrucciones de Juego', tabJuego ,background_color='#4f280a',),
                          sg.Tab('Iconos y Casilleros', tabIconCas,background_color='#4f280a',),
                          sg.Tab('Más', tabOtros,background_color='#4f280a',)]],
                           font=('Arial', 14),
                          key='pestanas', title_color='red',
                          selected_title_color='white', tab_location='top',theme=mi_tema())],
              [sg.Button('Cerrar',button_color=('black','#f75404'), font=('Arial', 16),size=(20,10),key='cerrar')]]

    mi_tema()
    ventana = sg.Window('Ayuda', layout=layout, element_justification='center',grab_anywhere=True,
                        size=(780,580)).Finalize()

    while True:

        eventos, valor = ventana.read()
        if eventos in (None, 'cerrar'):
            break
    ventana.close()



if __name__ == '__main__':
    ayuda()
