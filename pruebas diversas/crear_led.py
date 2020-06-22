from PIL import Image,ImageDraw
import PIL.ImageOps
import PySimpleGUI as sg


x=25
y=25
r=10
img = Image.new('RGB',(50,50),(255,255,255)) #crea una cuadrado blanco 20x20 color rgb
dibujo = ImageDraw.Draw(img) #va a dibujar sobre la imagen creada
dibujo.ellipse((x-r, y-r, x+r, y+r), fill=(225,0,0),outline=(255,0,0)) #dibuja un círculo verde con bode rojo
#img.show() #muestra la imagen
img.save('led.png')

rojo = False

contenido = [
    [sg.Image('led.png',key='led')],
    [sg.Button('Color',key='Color')]
]
windows = sg.Window('Led',layout=contenido)
while True:
    event, values = windows.read()
    
    if event in (None, 'Salir'):	# Salir, cierra ventana
        break
    if event == 'Color':
        if rojo == False:        
            dibujo.ellipse((x-r, y-r, x+r, y+r), fill=(255,0,0),outline=(255,0,0))
            rojo = True
        else:
            dibujo.ellipse((x-r, y-r, x+r, y+r), fill=(0,255,0),outline=(255,0,0))
            rojo = False    
        img.save('..\\led.png') 
        windows['led'].update('..\\led.png')  
    windows.Refresh()
windows.close()
#img = Image.open('D:\\Informatica\\cursos online\\python\\astral1.jpeg')
#img_volteada= PIL.ImageOps.invert(img)
#img_volteada.show()
#img_volteada.save('D:\\Informatica\\cursos online\\python\\astral_volteada.jpg')
'''
Cambia el color de una imagen

imgRGB = img.convert('RGB')
r,g,b = img.getpixel((1, 1))
color_a_cambiar = (r,g,b)
print(color_a_cambiar)
widht,height = img.size
pixels=img.load()
print(widht,height)
for x in range(widht):
    for y in range(height):
        r, g, b = pixels[x, y]         
#        if (r, g, b) == color_a_cambiar:
#            pixels[x, y] = (130,130,130)
        if (r,g,b) != color_a_cambiar:
            print (r,g,b)
'''

      