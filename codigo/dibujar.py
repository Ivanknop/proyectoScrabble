import PySimpleGUI as sg
from logica.tablero import *
from logica.configuracion import *
from logica.preferencias import Preferencias
from logica.atril import Atril
from logica.bolsa_fichas import *
import time

class Dibujar():
    '''Recibe objetos de tipo atril, tablero y preferencias e inicializa
    los distintos espacios de la GUI'''
    def __init__ (self, tablero, preferencias, atril):
        self._tiempo_inicio = 0
        self._tiempo_fin = 0
        #Prepara y agrega a la columna izquierda de la interfaz todos los casilleros del tablero
        columna_izquierda = []
        #Filas
        f = 0
        #Columnas
        c = 0
        for fila in tablero.getCasilleros():
            insercion = []
            for dato in fila:
                if (tablero.esFicha(ficha=dato)):
                    insercion.append(sg.Button(image_filename=f'ficha {list(dato.keys())[0]}.png', pad=(0,0), key=f'tablero {f},{c}', image_size=(29,31), enable_events=True))
                else:
                    if (dato==''):
                        insercion.append(sg.Button(image_filename='azul.png', pad=(0,0), key=f'tablero {f},{c}', image_size=(29,31), enable_events=True))
                    else:
                        insercion.append(sg.Button(image_filename=f'{dato[1:]}.png', pad=(0,0), key=f'tablero {f},{c}', image_size=(29,31), enable_events=True))
                c += 1
            f += 1
            c = 0
            columna_izquierda.append(insercion)

        fichas = []
        for i in range(0, atril.get_cant_fichas()):
            fichas.append(sg.Button(image_filename='ficha a.png', image_size=(29,31), key=f'ficha {str(i)}'))
        fichas_oponente = []
        for i in range(0, atril.get_cant_fichas()):
            fichas_oponente.append(sg.Button(image_filename='unaFichaOponente.png', image_size=(29,31), key=f'ficha_oponente {str(i)}'))

        columna_derecha = [[sg.Image('scrabbleArLogo.png')],
                            [sg.Text(f'Nivel: {preferencias.getNivel()}', font=('Arial', 14))],
                            [sg.Text('Puntuación actual:      ', font=('Arial', 14), key='puntaje')],
                            [sg.Text('Tiempo transcurrido:', font=('Arial', 14))],
                            [sg.Text('00:00', size=(15, 1), font=('Impact', 26), justification='center', text_color='white', key='timer', background_color='black')],
                            [sg.ProgressBar(max_value=0, orientation='horizontal', size=(30, 30), key='progreso')],
                            [sg.Text('_'*30)],
                            [sg.Text(' ---TUS FICHAS--- ', background_color='black', font=('Arial', 14), text_color='White', key='palabra')],
                            fichas,
                            [sg.Button('Validar', font=('Arial', 14), key='validar')],
                            [sg.Text('_'*30)],
                            [sg.Text(' ---FICHAS DEL OPONENTE--- ', background_color='black', font=('Arial', 14), text_color='White')],
                            fichas_oponente]

        #Crea la ventana y la muestra
        diseño = [[sg.Column(columna_izquierda), sg.Column(columna_derecha, element_justification='center', pad=(10, None))]]
        self._interfaz = sg.Window('ScrabbleAR', diseño)
        self._interfaz.Finalize()

    def setTimer(self, minutos):
        '''Setea la cantidad de tiempo disponible para jugar, recibida en el
        parámetro 'minutos'.
        Ejemplo: 0.5 = 30 segundos, 1 = 60 segundos, etc.'''
        #Establece el tiempo de inicio del juego
        self._setTiempoInicio(time.time())
        #Y el tiempo de finalización
        self._setTiempoFin(self._getTiempoInicio() + (minutos * 60))
        self._getInterfaz()['progreso'].UpdateBar(0, max=(self._getTiempoFin() - self._getTiempoInicio()))

    def actualizarTimer(self):
        '''Actualiza el timer en la interfaz.'''
        tiempo_actual = time.time() - self._getTiempoInicio()
        self._getInterfaz()['timer'].Update('{:02d}:{:02d}'.format(int(tiempo_actual // 60), int(tiempo_actual % 60)))
        self._getInterfaz()['progreso'].UpdateBar(self._getTiempoFin()-time.time())

    def terminoTimer(self):
        """
        Retorna True o False dependiendo de si el timer llegó a su tiempo límite.
        """
        return time.time() > self._getTiempoFin()

    def leer(self):
        '''Retorna en formato de tupla el último evento de la interfaz, si
        lo hubiese, y su respectivo valor. Si ningún evento ocurrió, el
        programa sigue su curso con normalidad.
        Los eventos posibles son:
        "tablero f,c", donde f y c son la fila y columna donde está el botón;
        "ficha i", donde i representa el número de ficha elegido, siendo i >= 0 & i <= cant_total_fichas'''
        return self._getInterfaz().Read(timeout=0)

    def actualizarTablero(self, tablero):
        '''Analiza la matriz y la proyecta en la GUI. Si durante el proceso
        se topa con una ficha, busca la imagen PNG que le corresponde.'''
        #Filas
        f = 0
        #Columnas
        c = 0
        for fila in tablero.getCasilleros():
            for dato in fila:
                if (tablero.esFicha(ficha=dato)):
                    self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename=f'ficha {list(dato.keys())[0]}.png', image_size=(29,31))
                else:
                    if (dato == ''):
                        self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename='azul.png', image_size=(29,31))
                    else:
                        self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename=f'{dato[1:]}.png', image_size=(29,31))
                c += 1
            c = 0
            f += 1

    def actualizarPuntaje(self, nuevo_puntaje):
        self._getInterfaz()['puntaje'].Update(f'Puntuación actual: {nuevo_puntaje}', font=('Arial', 14))

    def seleccionarOrientacion(self, coordenada, pref):
        '''Una vez validada la palabra, permite mostrar los botones para
        seleccionar su orientación. La coordenada recibida por parámetro, en
        formato string "f,c", se corresponde con la fila y columna del tablero
        a partir de las cuáles se seleccionará el sentido.
        Las preferencias son necesarias para no insertar un botón de
        "sentido" fuera del límite.'''
        f = int(coordenada.split(",")[0])
        c = int(coordenada.split(",")[1])
        self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename='orientacion.png', image_size=(29,31))
        c_contiguo = c + 1
        if (c_contiguo != pref.getColumnas()):
            self._getInterfaz()[f'tablero {f},{c_contiguo}'].Update(image_filename='orientacionDerecha.png', image_size=(29,31))
        f_inferior = f + 1
        if (f_inferior < pref.getFilas()):
            self._getInterfaz()[f'tablero {f_inferior},{c}'].Update(image_filename='orientacionAbajo.png', image_size=(29,31))

    def actualizarPalabra(self, palabra):
        self._getInterfaz()['palabra'].Update(palabra, background_color='black', font=('Arial', 14), text_color='White')

    def _getInterfaz(self):
        return self._interfaz
    def _setInterfaz(self, unaInterfaz):
        self._interfaz = unaInterfaz
    def _getTiempoInicio(self):
        return self._tiempo_inicio
    def _setTiempoInicio(self, segundos):
        self._tiempo_inicio = segundos
    def _getTiempoFin(self):
        return self._tiempo_fin
    def _setTiempoFin(self, segundos):
        self._tiempo_fin = segundos


confi = nivel_medio()
configu = Preferencias(confi['filas'],confi['columnas'],confi['especiales'], confi['nivel'])
unTablero = Tablero(configu)
bolsa_fichas = crear_bolsa(confi['cant_fichas'],confi['puntaje_ficha'])
jugador = Atril (bolsa_fichas, 7)
interfaz = Dibujar(unTablero, configu, jugador)

prueba_mostrar = True
interfaz.setTimer(1)

jugar = True
while jugar:
    event, value = interfaz.leer()
    if ('ficha' in event):
        palabra = ''
        validar = False
        palabra += list(jugador.get_ficha(int(event.split()[1])).keys())[0]
        interfaz.actualizarPalabra(palabra)
        while (not validar):
            event, value = interfaz.leer()
            if (event == 'validar'):
                validar = True
            if ('ficha' in event):
                palabra += list(jugador.get_ficha(int(event.split()[1])).keys())[0]
                interfaz.actualizarPalabra(palabra)
            interfaz.actualizarTimer()
        print('este evento terminó')
    if interfaz.terminoTimer():
        break
    interfaz.actualizarTimer()
