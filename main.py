from codigo.logica.tablero import *
from codigo.logica.configuracion import *
from codigo.logica.preferencias import Preferencias
from codigo.logica.atril import Atril
from codigo.logica.bolsa_fichas import *
from codigo.interfaz.dibujar import Dibujar
import codigo.logica.check_palabra as cp
from codigo.logica.guardar_partida import Juego_Guardado
import time
import random

configuracion = nivel_medio()
preferencias = Preferencias(configuracion['filas'],configuracion['columnas'],configuracion['especiales'], configuracion['nivel'])
unTablero = Tablero(preferencias)
bolsa_fichas = crear_bolsa(configuracion['cant_fichas'],configuracion['puntaje_ficha'])
jugador = Atril (bolsa_fichas, 7)

archivo_partida = Juego_Guardado()
if (archivo_partida.cargar_guardado()):
    puntaje = archivo_partida.getPuntaje()
    unTablero = archivo_partida.getTablero()
    jugador = archivo_partida.getAtril()
    bolsa_fichas = archivo_partida.getBolsaFichas()
    preferencias = archivo_partida.getPreferencias()
    turno_jugador = True
    cant_cambiar = archivo_partida.getCantCambiar()
    interfaz = Dibujar(unTablero, preferencias, jugador)
    puntaje_pc = archivo_partida.getPuntajePC()
    if (cant_cambiar == 0):
        interfaz.inhabilitarElemento('cambiar')
    interfaz.setTimer(archivo_partida.getTiempoRestante() / 60)
    interfaz.actualizarPuntajePC(puntaje_pc)
    interfaz.actualizarPuntaje(puntaje)
else:
    turno_jugador = random.choice([True, False])
    cant_cambiar = 3
    puntaje = 0
    puntaje_pc = 0
    atril_pc = Atril(bolsa_fichas, 7)
    interfaz = Dibujar(unTablero, preferencias, jugador)
    interfaz.setTimer(5)

jugar = True
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
                    cambio_posicion = False
                    while elegir_posicion:
                        if not (cambio_posicion):
                            event, value = interfaz.leer()
                        if (interfaz.terminoTimer()) or (event == None):
                            jugar = False
                            break
                        if 'tablero' in event:
                            interfaz.seleccionarOrientacion(event.split()[1], preferencias)
                            fila = event.split(" ")[1].split(',')[0]
                            columna = event.split(" ")[1].split(',')[1]
                            coord_derecha = fila + ',' + str(int(columna) + 1)
                            coord_inferior = str(int(fila) + 1) + ',' + columna
                            while True:
                                event, value = interfaz.leer()
                                if (interfaz.terminoTimer()) or (event == None):
                                    jugar = False
                                    break
                                if (event == f'tablero {coord_derecha}') or (event == f'tablero {coord_inferior}'):
                                    lista_insercion = []
                                    for f in fichas_seleccionadas:
                                        lista_insercion.append(jugador.get_ficha(f))
                                    puntaje_palabra = unTablero.insertarPalabra(lista_insercion, (int(fila),int(columna)), 'h' if event == f'tablero {coord_derecha}' else 'v')
                                    if puntaje_palabra == -1:
                                        interfaz.actualizarPalabra('NO HAY ESPACIO', color='red', fondo='white', tamaño=12)
                                    else:
                                        fichas_seleccionadas.sort(reverse=True)
                                        for f in fichas_seleccionadas:
                                            jugador.usar_ficha(f)
                                        jugador.llenar_atril(bolsa_fichas)
                                        puntaje += puntaje_palabra
                                        interfaz.actualizarPuntaje(puntaje)
                                        interfaz.textoEstandar()
                                        turno_jugador = False
                                    interfaz.actualizarAtril(jugador)
                                    interfaz.actualizarTablero(unTablero)
                                    elegir_posicion = False
                                    break
                                elif ('tablero' in event):
                                    cambio_posicion = True
                                    interfaz.reestablecerOrientacion(fila+','+columna, unTablero, preferencias)
                                    break
                                interfaz.actualizarTimer()
                        interfaz.actualizarTimer()
                else:
                    interfaz.actualizarPalabra('PALABRA NO VÁLIDA ¡PRUEBA DE NUEVO!', tamaño=10, color='red', fondo='white')
                    interfaz.actualizarAtril(jugador)
                if (event != None):
                    interfaz.habilitarElemento('guardar')
                    if (cant_cambiar > 0):
                        interfaz.habilitarElemento('cambiar')
        if (event == 'cambiar') and (cant_cambiar > 0):
            cant_cambiar = cant_cambiar - 1
            jugador.cambiar_fichas(bolsa_fichas)
            interfaz.actualizarAtril(jugador)
            if (cant_cambiar == 0):
                interfaz.inhabilitarElemento('cambiar')
            turno_jugador = False
        if event == 'guardar':
            instante = time.time()
            eleccion = interfaz.popUpOkCancel('¿Estas seguro que deseas guardar la partida?')
            interfaz.paralizarTimer(instante)
            if eleccion == 'OK':
                archivo_partida = Juego_Guardado(unTablero, 'NombreUsuario', jugador, bolsa_fichas, puntaje, puntaje_pc, interfaz.getTiempoRestante(), preferencias, cant_cambiar)
                archivo_partida.crear_guardado()
                jugar = False
        interfaz.actualizarTimer()
    #Si es el turno de la PC...
    else:
        if (interfaz.terminoTimer()):
            break
        mejor_opcion = cp.check_compu(atril_pc, unTablero)
        if len(mejor_opcion) != 0:
            puntaje_pc += unTablero.insertarPalabra(mejor_opcion['fichas'], mejor_opcion['coordenada'], mejor_opcion['sentido'])
            for ficha in mejor_opcion['fichas']:
                indice = atril_pc.ver_atril().index(ficha)
                atril_pc.usar_ficha(indice)
            atril_pc.llenar_atril(bolsa_fichas)
            interfaz.actualizarTablero(unTablero)
            interfaz.actualizarPuntajePC(puntaje_pc)
        turno_jugador = True
