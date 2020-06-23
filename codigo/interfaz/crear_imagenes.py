from PIL import Image,ImageDraw,ImageFont


def crear_imagen (car):
    '''
    Recibe un caracter que es el nombre de la imagen que debe utilizar. 
    Si se encuentra en la lista Caracteres, entonces crea una imagen de fondo marrón y le agrega una letra
    del mismo CAR que vino de parámetro
    Si no, revisa en la lista Especiales y si encuentra allí el elemento, crea las imágenes correspondientes
    En caso negativo, crea una imagen de error.
    '''
    
    caracteres=[]
    def _rango_letras(inicio, fin):
        for c in range(ord(inicio), ord(fin)+1):
            yield chr(c)
    for c in _rango_letras('A', 'Z'):
        caracteres.append(c)
    especiales = ['+','-','0','*','/']
    if car in caracteres:
        font = ImageFont.truetype("impact.ttf", 20) 
        img = Image.new('RGBA', (29,31), (128,64,0,255)) 
        dibujo = ImageDraw.Draw(img)
        dibujo.text((10, 5), car.upper(), 'white', font)
        img.save(f'\\ficha {car}.png')
    elif car in especiales:
        if car == '+':
            font = ImageFont.truetype("impact.ttf", 20) 
            img = Image.new('RGBA', (29,31), (255,128,0,255)) 
            dibujo = ImageDraw.Draw(img)
            dibujo.text((10, 5), car, 'white', font)
            img.save(f'\\ficha suma.png')
        if car == '-':
            font = ImageFont.truetype("impact.ttf", 20) 
            img = Image.new('RGBA', (29,31), (255,128,0,255))
            dibujo = ImageDraw.Draw(img)
            dibujo.text((10, 5), car, 'white', font)
            img.save(f'\\ficha resta.png')
        if car == '*':
            font = ImageFont.truetype("impact.ttf", 20) 
            img = Image.new('RGBA', (29,31), (255,128,0,255)) 
            dibujo = ImageDraw.Draw(img)
            dibujo.text((10, 5), car, 'white', font)
            img.save(f'\\ficha multiplica.png')
        if car == '/':
            font = ImageFont.truetype("impact.ttf", 20) 
            img = Image.new('RGBA', (29,31), (255,128,0,255)) 
            dibujo = ImageDraw.Draw(img)
            dibujo.text((10, 5), car, 'white', font)
            img.save(f'\\ficha divide.png')
        if car == '0':
            font = ImageFont.truetype("impact.ttf", 20) 
            img = Image.new('RGBA', (29,31), (255,255,255,0)) 
            dibujo = ImageDraw.Draw(img)
            img.save(f'\\ficha {car}.png')
    else:
        try:
            img = Image.open(f'\\ficha error.png')
        except:
            img = Image.new('RGBA',(200,200),(100,100,100,255))
            dibujo = ImageDraw.Draw(img)
            dibujo.line((0, 0) + img.size, fill=(255,0,0,255),width=3)
            dibujo.line((0, img.size[1], img.size[0], 0), fill=(255,0,0,255),width=3)
            img.save(f'\\ficha error.png')

    return img
