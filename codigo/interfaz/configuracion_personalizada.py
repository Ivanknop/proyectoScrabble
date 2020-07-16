import PySimpleGUI as sg

def layout():
    '''Diseña el layout de la ventana de configuración.
    Keys de los elementos: filas, columnas, tiempo,
    cantidades_x, puntajes_x (donde "x", una letra en mayúsculas),
    guardar, cancelar'''
    fuente_texto = 'Arial'
    tamaño_fuente = 12
    tamaño_letras = 10
    layout = [[sg.Text('Ajuste los valores de la configuración según lo desee', pad=((115, 0), (0, 0)), justification='center', font=('Italic', 16))],
                [sg.Text('Cantidad de filas: ', font=(fuente_texto, tamaño_fuente)), sg.Spin([i for i in range(5, 21)], initial_value=5, key='filas'), sg.Text('Cantidad de columnas: ', font=(fuente_texto, tamaño_fuente)), sg.Spin([i for i in range(5, 21)], initial_value=5, key='columnas'),
                sg.Text('Tiempo total (minutos): ', font=(fuente_texto, tamaño_fuente)), sg.Spin([i for i in range(5, 41)], key='tiempo')]]
    #Prepara los dos frames donde se configurará la cantidad de fichas de la bolsa y sus puntajes
    for objetivo in ['cantidades', 'puntajes']:
        frame_resultante = []
        fila = []
        #Cantidad de elementos a mostrar por fila del frame
        contador_salto = 5
        for i in range(ord('A'), ord('Z')+1):
            fila.extend([sg.Text(f'{chr(i)}: ', font=(fuente_texto, tamaño_letras)), sg.Spin([i for i in range(1, 31)], key=f'{objetivo}_{chr(i)}', size=(2, None))])
            #Dado que la N no suele preceder a la Ñ en la tabla ASCII, si llegué a la primera inserto la segunda a continuación
            if (chr(i) == 'N'):
                fila.extend([sg.Text('Ñ: ', font=(fuente_texto, tamaño_letras)), sg.Spin([i for i in range(1, 31)], key=f'{objetivo}_Ñ')])
                contador_salto = contador_salto - 1
            contador_salto = contador_salto - 1
            if (contador_salto < 1):
                frame_resultante.append(fila)
                fila = []
                contador_salto = 5
        if (len(fila) != 0):
            frame_resultante.append(fila)
        if (objetivo == 'cantidades'):
            layout.append([sg.Frame(layout=frame_resultante, font=('Italic 12'), title='Cantidad de fichas', element_justification='left')])
        else:
            #En el layout, toma la última lista que se insertó (la que contiene el primer frame) y le agrega el frame recién creado.
            #Esto causa que el espacio con los puntajes se vea a la derecha del de la bolsa, en lugar de debajo.
            layout[-1].extend([sg.Frame(layout=frame_resultante, font=('Italic 12'), title='Puntajes de las fichas', element_justification='right')])
    layout.append([sg.Button('Guardar y jugar', key='guardar'), sg.Button('Cancelar', key='cancelar')])
    return layout

def generar_configuracion(ventana, conf):
    '''Crea un diccionario con la información proporcionada por el usuario,
    su estructura es idéntica al de los niveles predeterminados.
    Además, controla que no se hayan ingresado datos incorrectos'''
    #Al inicio, se asume que no hay ningún error
    conf['error'] = ''
    conf['nivel'] = 'Personalizado'

    for spin in ['filas', 'columnas', 'tiempo']:
        valor_spin = ventana[f'{spin}'].Get()
        try:
            valor_spin = int(valor_spin)
        except:
            conf['error'] = 'Se asignó un valor no numérico a la cantidad de filas, columnas o al tiempo'
            return conf
        if (valor_spin < 1):
            conf['error'] = 'Se asignó un valor nulo o negativo a la cantidad de filas, columnas o al tiempo'
        conf[spin] = valor_spin

    cant_fichas = {}
    for frame in ['cantidades', 'puntajes']:
        for i in range(ord('A'), ord('Z')+2):
            letra = chr(i)
            if (i == (ord('Z') + 1)):
                letra = 'Ñ'
            #Obtiene el contenido del spin según el frame en el que se encuentre y la letra actual
            valor_spin = ventana[f'{frame}_{letra}'].Get()
            #Si se ingresó otro caracter que no sea un entero, se guardará el error y dejara de iterar
            try:
                valor_spin = int(valor_spin)
            except:
                conf['error'] = f'Se asignó un valor no numérico a la letra {letra} en el espacio de {frame}'
                return conf
            #Si se ingreso un entero no valido, hará lo mismo que en el paso anterior
            if (valor_spin < 1):
                conf['error'] = f'La letra {letra} posee valor nulo o negativo en el espacio de {frame}'
                return conf
            cant_fichas[f'{letra}'] = valor_spin
    conf['cant_fichas'] = cant_fichas

    return conf


def interfaz_personalizacion():
    '''Muestra la interfaz de configuración y controla sus eventos'''
    conf = {}
    ventana = sg.Window('Configuración personalizada', layout())
    ventana.Finalize()
    while True:
        event, values = ventana.Read()
        if (event in (None, 'cancelar')):
            break
        if (event == 'guardar'):
            configuracion = generar_configuracion(ventana, conf)
            print(configuracion)
            break
    return conf

if __name__ == '__main__':
    interfaz_personalizacion()
