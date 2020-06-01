import PySimpleGUI as sg
from logica.tablero import *
from logica.configuracion import *
from logica.preferencias import Preferencias
from logica.atril import Atril
from logica.bolsa_fichas import *
import logica.check_palabra as cp
from logica.guardar_partida import Juego_Guardado
import time
import random

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
            letra = list(atril.get_ficha(i).keys())[0]
            fichas.append(sg.Button(image_filename=f'ficha {letra}.png', image_size=(29,31), key=f'ficha {str(i)}'))
        fichas_oponente = []
        for i in range(0, atril.get_cant_fichas()):
            fichas_oponente.append(sg.Button(image_filename='unaFichaOponente.png', image_size=(29,31), key=f'oponente {str(i)}'))

        columna_derecha = [[sg.Image('scrabbleArLogo.png')],
                            [sg.Text(f'Nivel: {preferencias.getNivel()}', font=('Arial', 14))],
                            [sg.Text('Puntuación actual: 0    ', font=('Arial', 14), key='puntaje')],
                            [sg.Text('Tiempo transcurrido:', font=('Arial', 14))],
                            [sg.Text('00:00', size=(15, 1), font=('Impact', 26), justification='center', text_color='white', key='timer', background_color='black')],
                            [sg.ProgressBar(max_value=0, orientation='horizontal', size=(30, 30), key='progreso')],
                            [sg.Text('_'*30)],
                            [sg.Text('              ---TUS FICHAS---             ', background_color='black', font=('Arial', 14), text_color='White', key='palabra')],
                            fichas,
                            [sg.Button('Validar', font=('Arial', 12), key='validar'), sg.Button('Cambiar fichas', font=('Arial', 12), key='cambiar')],
                            [sg.Text('_'*30)],
                            [sg.Text('    ---FICHAS DEL OPONENTE---    ', background_color='black', font=('Arial', 14), text_color='White')],
                            fichas_oponente,
                            [sg.Button('Guardar y salir', font=('Arial', 12), key='guardar')]]

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
        '''Retorna True o False dependiendo de si el timer llegó a su tiempo límite.'''
        return time.time() > self._getTiempoFin()

    def paralizarTimer(self, instante):
        '''Recibe el instante, en segundos, a partir del cual se dejó de tener
        en cuenta el timer. Luego, cálcula el tiempo perdido desde ese momento
        hasta la llamada de la función, y lo añade al tiempo de inicio y final,
        permitiendo reestablecer el cronómetro como si no hubiera avanzado el tiempo.
        Retorna el momento siguiente a ese cálculo.
        Si el resultado se utiliza en un búcle, el timer se paraliza indefinidamente'''
        if instante < time.time():
            instante = time.time() - instante
            interfaz._setTiempoInicio(interfaz._getTiempoInicio() + instante)
            interfaz._setTiempoFin(interfaz._getTiempoFin() + instante)
            instante = time.time()
        return instante

    def getTiempoRestante(self):
        return self._getTiempoFin() - time.time()

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

    def actualizarAtril(self, atril):
        for f in range(0, atril.get_cant_fichas()):
            letra = list(atril.get_ficha(f).keys())[0]
            self._getInterfaz()[f'ficha {f}'].Update(image_filename=f'ficha {letra}.png', image_size=(29,31), disabled=False)


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

    def actualizarPalabra(self, palabra, color=None, fondo=None, tamaño=14):
        self._getInterfaz()['palabra'].Update(palabra, font=('Arial', tamaño), text_color=color, background_color=fondo)

    def textoEstandar(self):
        self._getInterfaz()['palabra'].Update('              ---TUS FICHAS---             ', background_color='black', font=('Arial', 14), text_color='White')

    def inhabilitarElemento(self, clave):
        self._getInterfaz()[clave].Update(disabled=True)

    def habilitarElemento(self, clave):
        self._getInterfaz()[clave].Update(disabled=False)

    def popUp(self, cadena):
        sg.popup(cadena, keep_on_top=True)

    def popUpOkCancel(self, cadena):
        return sg.popup_ok_cancel(cadena, keep_on_top=True)

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


jugar = True
#turno_jugador = random.choice([True, False])
cant_cambiar = 3
turno_jugador = True
puntaje = 0

archivo_partida = Juego_Guardado()
if (archivo_partida.cargar_guardado()):
    puntaje = archivo_partida.getPuntaje()
    unTablero = archivo_partida.getTablero()
    jugador = archivo_partida.getAtril()
    bolsa_fichas = archivo_partida.getBolsaFichas()
    configu = archivo_partida.getPreferencias()
    turno_jugador = True
    cant_cambiar = archivo_partida.getCantCambiar()
    interfaz = Dibujar(unTablero, configu, jugador)
    if (cant_cambiar == 0):
        interfaz.inhabilitarElemento('cambiar')
    interfaz.setTimer(archivo_partida.getTiempoRestante() / 60)
    interfaz.actualizarPuntaje(puntaje)
else:
    interfaz = Dibujar(unTablero, configu, jugador)
    interfaz.setTimer(1)


while jugar:
    if (turno_jugador):
        event, value = interfaz.leer()
        if interfaz.terminoTimer():
            jugar = False
            break
        if event == None:
            break
        if ('ficha' in event):
            fichas_seleccionadas = []
            fichas_seleccionadas.append(int(event.split(" ")[1]))
            palabra = ''
            click_validar = False
            palabra += list(jugador.get_ficha(int(event.split()[1])).keys())[0]
            interfaz.actualizarPalabra(palabra)
            interfaz.inhabilitarElemento(event)
            interfaz.inhabilitarElemento('guardar')
            interfaz.inhabilitarElemento('cambiar')
            while (not click_validar):
                event, value = interfaz.leer()
                if (interfaz.terminoTimer()) or (event == None):
                    jugar = False
                    break
                if (event == 'validar'):
                    click_validar = True
                if ('ficha' in event):
                    fichas_seleccionadas.append(int(event.split(" ")[1]))
                    interfaz.inhabilitarElemento(event)
                    palabra += list(jugador.get_ficha(int(event.split()[1])).keys())[0]
                    interfaz.actualizarPalabra(palabra)
                interfaz.actualizarTimer()
            if (click_validar):
                if(cp.check_jugador(palabra)):
                    interfaz.actualizarPalabra('SELECCIONE DÓNDE INSERTAR', tamaño=12, color='green', fondo='white')
                    elegir_posicion = True
                    while elegir_posicion:
                        event, value = interfaz.leer()
                        if (interfaz.terminoTimer()) or (event == None):
                            jugar = False
                            break
                        if 'tablero' in event:
                            interfaz.seleccionarOrientacion(event.split()[1], configu)
                            elegir_orientacion = True
                            fila = event.split(" ")[1].split(',')[0]
                            columna = event.split(" ")[1].split(',')[1]
                            coord_derecha = fila + ',' + str(int(columna) + 1)
                            coord_inferior = str(int(fila) + 1) + ',' + columna
                            while elegir_orientacion:
                                event, value =interfaz.leer()
                                if (interfaz.terminoTimer()) or (event == None):
                                    jugar = False
                                    break
                                if (event == f'tablero {coord_derecha}') or (event == f'tablero {coord_inferior}'):
                                    lista_insercion = []
                                    for f in fichas_seleccionadas:
                                        lista_insercion.append(jugador.get_ficha(f))
                                    puntaje_palabra = unTablero.insertarPalabra(lista_insercion, (int(fila),int(columna)), 'h' if event == f'tablero {coord_derecha}' else 'v')
                                    elegir_orientacion = False
                                    if puntaje_palabra == -1:
                                        interfaz.actualizarPalabra('NO HAY ESPACIO', color='red', fondo='white')
                                    else:
                                        fichas_seleccionadas.sort(reverse=True)
                                        for f in fichas_seleccionadas:
                                            jugador.usar_ficha(f)
                                        jugador.llenar_atril(bolsa_fichas, 7)
                                        puntaje += puntaje_palabra
                                        interfaz.actualizarPuntaje(puntaje)
                                    interfaz.actualizarAtril(jugador)
                                    interfaz.textoEstandar()
                                    interfaz.actualizarTablero(unTablero)
                                    elegir_posicion = False
                                    break
                                interfaz.actualizarTimer()
                        interfaz.actualizarTimer()
                else:
                    interfaz.actualizarPalabra('PALABRA NO VÁLIDA ¡PRUEBA DE NUEVO!', tamaño=10, color='red', fondo='white')
                    interfaz.actualizarAtril(jugador)
                turno_jugador = False
                if (event != None):
                    interfaz.habilitarElemento('guardar')
                    if (cant_cambiar > 0):
                        interfaz.habilitarElemento('cambiar')
        if (event == 'cambiar') and (cant_cambiar > 0):
            cant_cambiar = cant_cambiar - 1
            jugador.cambiar_fichas(bolsa_fichas, 7)
            interfaz.actualizarAtril(jugador)
            if (cant_cambiar == 0):
                interfaz.inhabilitarElemento('cambiar')
            turno_jugador = False
        if event == 'guardar':
            instante = time.time()
            eleccion = interfaz.popUpOkCancel('¿Estas seguro que deseas guardar la partida?')
            interfaz.paralizarTimer(instante)
            if eleccion == 'OK':
                archivo_partida = Juego_Guardado(unTablero, 'NombreUsuario', jugador, bolsa_fichas, puntaje, interfaz.getTiempoRestante(), configu, cant_cambiar)
                archivo_partida.crear_guardado()
                jugar = False
        interfaz.actualizarTimer()
    #Si es el turno de la PC...
    else:
        time.sleep(2)
        print ('Juega la pc')
        turno_jugador = True
