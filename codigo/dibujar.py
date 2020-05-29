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
        #Prepara y agrega a la columna izquierda todos los casilleros del tablero
        columna_izquierda = []
        x = 0
        y = 0
        for fila in tablero.getCasilleros():
            insercion = []
            for dato in fila:
                if (dato==''):
                    insercion.append(sg.Button(image_filename='azul.png', pad=(0,0), key=f'tablero {x}{y}', image_size=(29,31), enable_events=True))
                else:
                    insercion.append(sg.Button(image_filename=f'{dato[1:]}.png', pad=(0,0), key=f'tablero {x}{y}', image_size=(29,31), enable_events=True))
                y += 1
            y = 0
            x += 1
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
                            [sg.Text('Tiempo transcurrido:', font=('Impact', 14))],
                            [sg.Text('00:00', size=(15, 1), font=('Impact', 26), justification='center', text_color='white', key='timer', background_color='black')],
                            [sg.Text('_'*30)],
                            [sg.Text(' ---TUS FICHAS--- ', background_color='black', font=('Arial', 14), text_color='White')],
                            fichas,
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

    def actualizarTimer(self):
        '''Actualiza el timer en la interfaz.'''
        tiempo_actual = time.time() - self._getTiempoInicio()
        self._getInterfaz()['timer'].Update('{:02d}:{:02d}'.format(int(tiempo_actual // 60), int(tiempo_actual % 60)))

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
        "tablero {x}{y}", donde x e y son las coordenadas del botón;
        "ficha {i}", donde i representa el número de ficha elegido, siendo i >= 0 & i <= cant_total_fichas'''
        return self._getInterfaz().Read(timeout=0)

    def actualizarTablero(self, tablero):
        '''Analiza la matriz y la proyecta en la GUI. Si durante el proceso
        se topa con una ficha, busca la imagen PNG que le corresponde.'''
        x = 0
        y = 0
        for fila in tablero.getCasilleros():
            for dato in fila:
                if (tablero.esFicha(ficha=dato)):
                    self._getInterfaz()[f'tablero {x}{y}'].Update(image_filename=f'ficha {list(dato.keys())[0]}.png', image_size=(29,31))
                y += 1
            y = 0
            x += 1

    def actualizarPuntaje(self, nuevo_puntaje):
        self._getInterfaz()['puntaje'].Update(f'Puntuación actual: {nuevo_puntaje}', font=('Arial', 14))

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
configuracion = Preferencias(confi['filas'],confi['columnas'],confi['especiales'], confi['nivel'])
unTablero = Tablero(configuracion)
bolsa_fichas = crear_bolsa(confi['cant_fichas'],confi['puntaje_ficha'])
jugador = Atril (bolsa_fichas, 7)
interfaz = Dibujar(unTablero, configuracion, jugador)
unTablero.insertarPalabra([{'a': 4}, {'a': 4}], (2, 2), 'h')
prueba_mostrar = True
interfaz.setTimer(1)

while True:
    event, value = interfaz.leer()
    if prueba_mostrar:
        interfaz.actualizarTablero(unTablero)
        interfaz.actualizarPuntaje(9)
        prueba_mostrar = False
    if event == 'tablero 01':
        interfaz.actualizarPuntaje(12)
    if interfaz.terminoTimer():
        break
    interfaz.actualizarTimer()
