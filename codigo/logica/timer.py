import time
import PySimpleGUI as sg
        
contenido = [
    [sg.Text('00:00', size=(30, 1), font=('Impact', 30), justification='center', text_color='white', key='text', background_color='black')],
]
ventana = sg.Window('Reloj',layout=contenido)
tiempo_actual = 0
empezar = True
tiempo_inicio = int(round(time.time() * 100))
while True:
    if empezar:      
        #esto debe extraerse de la dificultad
        tiempo = (int (input('Ingrese el tiempo límite en minutos'))*6000)
        empezar = False
    if tiempo_actual > tiempo:
        print('Tiempo Fuera')
        break
    else:
        event, values = ventana.Read(timeout=0)
        tiempo_actual = int(round(time.time() * 100)) - tiempo_inicio
        ventana.FindElement('text').Update('{:02d}:{:02d}'.format((tiempo_actual // 100) // 60,(tiempo_actual // 100) % 60))                                                            
ventana.Close()
