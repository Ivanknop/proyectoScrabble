from PIL import Image
import sys

try:
    img = Image.open ('D:\Informatica\Seminario Lenguaje Python\Scrabble-master\codigo\logica\\Ficha-2.png')
except:
    print ('Error')
    sys.exit(1)
'''
¿Cómo funciona esto?
0) Hay que instalar la librería pip install pil
1) Intenta abrir la imagen, si no la encuentra tira error y sale sin crashear
2) Extrae las dimensiones de la imagen en píxeles
3) Las reduce en proporción a ojo, debería hacerse en porcentaje
4) NO ES NECESARIO GUARDAR LAS IMAGENES MODIFICADAS

'''
otro_size = (37,39)
img4 = img.resize(otro_size)
img4.show()
#img.show() #muestra en pantalla la imagen
x,y = img.size #extrae las medidas en pixeles
print ('Alto: ',y)
print ('Ancho: ',x)
nuevo_size = (26,28) 
img2 = img.resize (nuevo_size) #crea nueva imagen redimensionada
print (img2.size)
img2.show()
#img2.save('Ficha-2-redimensionada.png') 
#Todas las imágenes son de 37,39
#img3 = img.resize(otro_size)
#img3.show()
#img3.save('otra-ficha-2.png') 