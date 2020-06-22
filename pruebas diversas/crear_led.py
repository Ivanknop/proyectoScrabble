from PIL import Image,ImageDraw
import PIL.ImageOps
import PySimpleGUI as sg


x=25
y=25
r=10
img = Image.new('RGBA',(50,50),(0,0,0,0)) #crea una cuadrado blanco 20x20 color rgb
dibujo = ImageDraw.Draw(img) #va a dibujar sobre la imagen creada
dibujo.ellipse((x-r, y-r, x+r, y+r), fill=(225,0,0,255),outline=(255,0,0,255)) #dibuja un círculo verde con bode rojo
#img.show() #muestra la imagen
img.save('D:\\Informatica\\cursos online\\python\\led.png')

rojo = False

contenido = [
    [sg.Image('D:\\Informatica\\cursos online\\python\\led.png',key='led')],
    [sg.Button('Color',key='Color')]
]
windows = sg.Window('Led',layout=contenido)
while True:
    event, values = windows.read()
    
    if event in (None, 'Salir'):	# Salir, cierra ventana
        break
    if event == 'Color':
        if rojo == False:        
            dibujo.ellipse((x-r, y-r, x+r, y+r), fill=(255,0,0,255),outline=(255,0,0,255))
            rojo = True
        else:
            dibujo.ellipse((x-r, y-r, x+r, y+r), fill=(0,255,0,225),outline=(255,0,0,255))
            rojo = False    
        img.save('D:\\Informatica\\cursos online\\python\\led.png') 
        windows['led'].update('D:\\Informatica\\cursos online\\python\\led.png')  
    windows.Refresh()
windows.close()

      
