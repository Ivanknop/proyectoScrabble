from PIL import Image, ImageDraw, ImageFont
'''
    Crea una imagen roja vacía
'''
#img = Image.new('RGB',(200,200),(255,0,0)) #crea objeto image
#img.save('cuadradorojo.png') #guarda en memoria secundaria

'''
Crea una letra y a su alrededor una imagen de fondo
'''
font = ImageFont.truetype("arial.ttf", 25) #carga en font una tipografía
#unicode_texto = u"A"
ancho, alto = font.getsize('B')
img2 = Image.new('RGB', (29,31), (255,0,0)) #crea un objeto image nuevo tomando las medidas de la font
dibujo = ImageDraw.Draw(img2)
dibujo.text((5, 5), u'A', 'white', font,justification='center')

img2.show() #muestra en pantalla 
#img2.save('cuadradoconletra.png') #guarda en memoria secundaria