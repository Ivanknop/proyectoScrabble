import PySimpleGUI as sg
import time
import os.path

class Dibujar():
    '''Recibe objetos de tipo atril, tablero y preferencias e inicializa
    los distintos espacios de la GUI'''

    def __init__ (self, tablero, preferencias, atril):

        # algunos valores por defecto para construir la interfaz del tablero
        # --------------------------
        self.tamcas = (37, 39)
        self.padin = (0, 0)
        self.botoncolor = ('white','#ece6eb')

        # --------------------------
        self._tiempo_inicio = 0
        self._tiempo_fin = 0
        self._ficha_tamano = (39,41)
        #Prepara y agrega a la columna izquierda de la interfaz todos los casilleros del tablero
        columna_izquierda = []
        #Filas
        f = 0
        #Columnas
        c = 0
        self._directorio_media = os.path.join('media', '')
        self._directorio_fichas = os.path.join('media', 'Fichas y espacios', '')
        for fila in tablero.getCasilleros():
            insercion = []
            for dato in fila:
                if (tablero.esFicha(ficha=dato)):
                    insercion.append(sg.Button(image_filename=f'{self._directorio_fichas}ficha {list(dato.keys())[0]}.png', pad=self.padin, key=f'tablero {f},{c}', image_size=self.tamcas,button_color=self.botoncolor, enable_events=True))
                else:
                    if (dato==''):
                        insercion.append(sg.Button(image_filename=f'{self._directorio_fichas}azul.png', pad=self.padin, key=f'tablero {f},{c}', image_size=self.tamcas, button_color=self.botoncolor,enable_events=True))
                    else:
                        insercion.append(sg.Button(image_filename=f'{self._directorio_fichas}{dato[1:]}.png', pad=self.padin, key=f'tablero {f},{c}', image_size=self.tamcas,button_color=self.botoncolor ,enable_events=True))
                c += 1
            f += 1
            c = 0
            columna_izquierda.append(insercion)

        fichas = []
        for i in range(0, atril.get_cant_fichas()):
            letra = list(atril.get_ficha(i).keys())[0]
            fichas.append(sg.Button(image_filename=f'{self._directorio_fichas}ficha {letra}.png', key=f'ficha {str(i)}', pad=(0, None), image_size=self._ficha_tamano))
        fichas_oponente = []
        for i in range(0, atril.get_cant_fichas()):
            fichas_oponente.append(sg.Button(image_filename=f'{self._directorio_fichas}unaFichaOponente.png', pad=(0, None), image_size=self._ficha_tamano, key=f'oponente {str(i)}'))

        columna_derecha = [[sg.Image(f'{self._directorio_media}scrabbleArLogo.png')],
                            [sg.Text(f'Nivel: {preferencias.getNivel()}', font=('Arial', 14))],
                            [sg.Text('Puntuación jugador: 0    ', font=('Arial', 14), key='puntaje')],
                            [sg.Text('Puntuación PC: 0    ', font=('Arial', 14), key='puntaje_pc')],
                            [sg.Text('Tiempo transcurrido:', font=('Arial', 14))],
                            [sg.Text('00:00', size=(15, 1), font=('Impact', 26), justification='center', text_color='white', key='timer', background_color='black')],
                            [sg.ProgressBar(max_value=0, orientation='horizontal', size=(30, 30), key='progreso')],
                            [sg.Text('_'*30)],
                            [sg.Text('                    ---TUS FICHAS---                  ', background_color='black', font=('Arial', 14), text_color='White', key='textoJugador')],
                            fichas,
                            [sg.Button('Validar', font=('Arial', 12), key='validar'), sg.Button('Cambiar fichas', font=('Arial', 12), key='cambiar')],
                            [sg.Text('_'*30)],
                            [sg.Text('          ---FICHAS DEL OPONENTE---       ', background_color='black', font=('Arial', 14), text_color='White', key='textoPC')],
                            fichas_oponente,
                            [sg.Button('Guardar y salir', font=('Arial', 12), key='guardar')]]

        #Crea la ventana y la muestra
        diseño = [[sg.Column(columna_izquierda,background_color='#ece6eb'), sg.Column(columna_derecha, element_justification='center', pad=(10, None))]]
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
            self._setTiempoInicio(self._getTiempoInicio() + instante)
            self._setTiempoFin(self._getTiempoFin() + instante)
            instante = time.time()
        return instante

    def getTiempoRestante(self):
        '''Devuelve el tiempo que falta para que termine la partida'''
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
                    self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename=f'{self._getDirectorioFicha()}ficha {list(dato.keys())[0]}.png', image_size=self.tamcas)
                else:
                    if (dato == ''):
                        self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename=f'{self._getDirectorioFicha()}azul.png' , image_size=self.tamcas)
                    else:
                        self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename=f'{self._getDirectorioFicha()}{dato[1:]}.png' , image_size=self.tamcas)
                c += 1
            c = 0
            f += 1

    def actualizarAtril(self, atril):
        for f in range(0, atril.get_cant_fichas()):
            letra = list(atril.get_ficha(f).keys())[0]
            self._getInterfaz()[f'ficha {f}'].Update(image_filename=f'{self._getDirectorioFicha()}ficha {letra}.png', disabled=False, image_size=self._getFichaTamano())
        if (atril.get_cant_fichas() < atril.getCantMaxima()):
            for f in range(atril.get_cant_fichas(), atril.getCantMaxima()):
                self.borrarElemento(f'ficha {f}')



    def actualizarPuntaje(self, nuevo_puntaje):
        self._getInterfaz()['puntaje'].Update(f'Puntuación jugador: {nuevo_puntaje}', font=('Arial', 14))

    def actualizarPuntajePC(self, nuevo_puntaje):
        self._getInterfaz()['puntaje_pc'].Update(f'Puntuación PC: {nuevo_puntaje}', font=('Arial', 14))

    def seleccionarOrientacion(self, coordenada, pref):
        '''Una vez validada la palabra, permite mostrar los botones para
        seleccionar su orientación. La coordenada recibida por parámetro, en
        formato string "f,c", se corresponde con la fila y columna del tablero
        a partir de las cuáles se seleccionará el sentido.
        Las preferencias son necesarias para no insertar un botón de
        "sentido" fuera del límite.'''
        f = int(coordenada.split(",")[0])
        c = int(coordenada.split(",")[1])
        self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename=f'{self._getDirectorioFicha()}orientacion.png', image_size=(29,31))
        c_contiguo = c + 1
        if (c_contiguo < pref.getColumnas()):
            self._getInterfaz()[f'tablero {f},{c_contiguo}'].Update(image_filename=f'{self._getDirectorioFicha()}orientacionDerecha.png', image_size=(29,31))
        f_inferior = f + 1
        if (f_inferior < pref.getFilas()):
            self._getInterfaz()[f'tablero {f_inferior},{c}'].Update(image_filename=f'{self._getDirectorioFicha()}orientacionAbajo.png', image_size=(29,31))

    def reestablecerOrientacion(self, coordenada, tablero, preferencias):
        '''Desvanece los botones de selección de orientación en la coordenada
        "f,c" indicada. Además, utiliza el tablero (que lo recibe como parámetro)
        para conocer lo que había en ese casillero, y las preferencias para no
        intentar reestablecer un botón de "sentido" fuera del límite.'''
        casilleros = tablero.getCasilleros()
        f = int(coordenada.split(",")[0])
        c = int(coordenada.split(",")[1])
        reestablecer = [{'f': f, 'c': c}, {'f': f, 'c': c + 1}, {'f': f + 1, 'c': c}]
        for coords in reestablecer:
            f = coords['f']
            c = coords['c']
            if (f < preferencias.getFilas()) and (c < preferencias.getColumnas()):
                if (tablero.esFicha(f=f, c=c)):
                    self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename=f'{self._getDirectorioFicha()}ficha {list(casilleros[f][c].keys())[0]}.png', image_size=(29,31))
                elif (casilleros[f][c] == ''):
                    self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename=f'{self._getDirectorioFicha()}azul.png', image_size=(29,31))
                else:
                    self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename=f'{self._getDirectorioFicha()}{casilleros[f][c][1:]}.png', image_size=(29,31))

    def actualizarTexto(self, texto, color=None, fondo=None, tamaño=14, pc=False):
        self._getInterfaz()['textoJugador' if not pc else 'textoPC'].Update(texto, font=('Arial', tamaño), text_color=color, background_color=fondo)

    def textoEstandar(self, pc=False):
        if pc == False:
            self._getInterfaz()['textoJugador'].Update('                    ---TUS FICHAS---                  ', background_color='black', font=('Arial', 14), text_color='White')
        else:
            self._getInterfaz()['textoPC'].Update('          ---FICHAS DEL OPONENTE---       ', background_color='black', font=('Arial', 14), text_color='White')

    def inhabilitarElemento(self, clave):
        self._getInterfaz()[clave].Update(disabled=True)

    def habilitarElemento(self, clave):
        self._getInterfaz()[clave].Update(disabled=False)

    def borrarElemento(self, clave):
        self._getInterfaz()[clave].Update(visible=False)

    def habilitarFinalizacion(self):
        self._getInterfaz()['cambiar'].Update('Finalizar juego')

    def popUp(self, cadena):
        sg.popup(cadena, keep_on_top=True)

    def popUpOkCancel(self, cadena):
        return sg.popup_ok_cancel(cadena, keep_on_top=True)

    def _getDirectorioFicha(self):
        return self._directorio_fichas
    def _getDirectorioMedia(self):
        return self._directorio_media
    def _getFichaTamano(self):
        return self._ficha_tamano
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
