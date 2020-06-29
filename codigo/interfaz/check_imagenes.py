from PIL import Image,ImageDraw,ImageFont
import PySimpleGUI as sg
import time
import os.path

def crear_ficha (ficha,directorio):
    '''
    Recibe una ficha y el directorio donde debe estar almacenada.
    Avalúa si es así. En caso contrario, crea una imagen nueva
    '''
    font = ImageFont.truetype("impact.ttf", 20) 
    img = Image.new('RGBA', (29,31), (128,64,0,255)) 
    dibujo = ImageDraw.Draw(img)
    dibujo.text((10, 5), ficha.upper(), 'white', font)
    img.save(f'{directorio}ficha {ficha}.png')
    return img

def crear_especial(esp,directorio):
    '''
    Recibe un casillero y el directorio donde debe estar almacenado.
    Avalúa si es así. En caso contrario, crea una imagen nueva
    '''
    font = ImageFont.truetype("impact.ttf", 20) 
    img = Image.new('RGBA', (29,31), (255,128,0,255)) 
    dibujo = ImageDraw.Draw(img)
    if esp == 'sum':
        dibujo.text((10, 5), '+', 'white', font)
    elif esp == 'rest':
        dibujo.text((10, 5), '-', 'white', font)
    elif esp == 'mult':
        dibujo.text((10, 5), '*2', 'white', font)
    elif esp == 'div':
        dibujo.text((10, 5), '/', 'white', font)
    elif esp == '0':
        img = Image.new('RGBA', (29,31), (255,255,255,0))
        dibujo = ImageDraw.Draw(img) 
        dibujo.text((10, 5), '0', 'black', font)
    elif esp == 'orientacionAbajo':
        img = Image.new('RGBA', (29,31), (125,125,125,0)) 
        dibujo = ImageDraw.Draw(img)
        dibujo.text((10, 5), '=>', 'black', font)
        img = img.rotate (270)
    elif esp == 'orientacionDerecha':
        img = Image.new('RGBA', (29,31), (255,0,255,0)) 
        dibujo = ImageDraw.Draw(img)
        dibujo.text((10, 5), '=>', 'black', font)
    elif esp == 'orientacion' or 'unaFichaOponente': 
        try:
            img = Image.open(f'{directorio}{esp}.png')
        except:
            img = Image.new('RGBA',(29,31),(100,100,100,255))
            dibujo.line((0, 0) + img.size, fill=(255,0,0,255),width=3)
            dibujo.line((0, img.size[1], img.size[0], 0), fill=(255,0,0,255),width=3)
    img.save(f'{directorio}{esp}.png')
    return img

def crear_avatar(av,directorio):
    '''
    Recibe un avatar y el directorio donde debe estar almacenado.
    Avalúa si es así. En caso contrario, crea una imagen nueva
    '''
    try:
        img = Image.open(f'{directorio}avatarError.png')
    except:
        img = Image.new('RGBA',(200,200),(100,100,100,255))
        dibujo = ImageDraw.Draw(img)
        dibujo.line((0, 0) + img.size, fill=(255,0,0,255),width=3)
        dibujo.line((0, img.size[1], img.size[0], 0), fill=(255,0,0,255),width=3)
        img.save(f'{directorio}avatarError.png')
     return img

def crear_error ():
    directorio = os.path.join('media', 'media_ii','')
    try:
        img = Image.open(f'{directorio}imagenError.png')
    except:
        img = Image.new('RGBA',(400,20),(79,40,10,255))
        font = ImageFont.truetype("arial.ttf", 12) 
        dibujo = ImageDraw.Draw(img)
        dibujo.text((12, 5), 'ALERTA, ALGÚN ARCHIVO DE IMAGEN ESTA DAÑADO O FALTA', 'white', font,align='center')
        img.save(f'{directorio}imagenError.png')
    return img
    
def crear_varios (imagen,directorio):
    '''
    Este va a trabajar con el resto de las imagenes, tipo logo y otros
    '''
    try:
        img = Image.open(f'\\ficha error.png')
    except:
        img = Image.new('RGBA',(200,200),(100,100,100,255))
        dibujo = ImageDraw.Draw(img)
        dibujo.line((0, 0) + img.size, fill=(255,0,0,255),width=3)
        dibujo.line((0, img.size[1], img.size[0], 0), fill=(255,0,0,255),width=3)
        img.save(f'{directorio}ficha error.png')
    return img

def check_fichas ():
    fichas=[chr(i) for i in range(ord('a'),ord('z')+1)]
    directorio = os.path.join('media', 'Fichas y espacios', '')
    errores = 0
    for i in range(len(fichas)):    
        try:
            img = Image.open (f'{directorio}ficha {fichas[i]}.png')
        except:
            img = crear_ficha(fichas[i],directorio)
            errores += 1
    return errores

def check_especiales ():
    especiales = ['sum','rest','0','div','mult','azul','orientacion','orientacionAbajo','orientacionDerecha','unaFichaOponente']
    directorio = os.path.join('media', 'Fichas y espacios', '')
    errores = 0
    for i in range(len(especiales)):    
        try:
            img = Image.open (f'{directorio}{especiales[i]}.png')
        except:
            img = crear_especial(especiales[i],directorio)
            errores += 1
    return errores  

def check_avatares():
    avatar = ['avatar1','avatar2','avatar3','avatar4','avatar7','avatar6']
    directorio = os.path.join('media', 'media_ii', 'avatars', '')
    errores = '0'
    for i in range (len(avatar)):
        try:
            img = Image.open (f'{directorio}{avatar[i]}.png')
        except:
            img = crear_avatar(avatar[i],directorio)
            errores = errores + ' ' + avatar[i]
    return errores

def loading():
    img_logo = os.path.join('media', 'scrabbleArLogo.png')
    contenido = [[sg.Image(img_logo, background_color='#4f280a')],
                [sg.Text(font=('Arial',12),size=(20,5),justification='center',
                background_color='#4f280a',text_color = 'yellow',key='texto')],
                [sg.Text(font=('Arial',12),size=(20,5),justification='center',
                background_color='#4f280a',text_color = 'yellow',key='ok')]
                ]
    v = sg.Window('Loading',layout=contenido,size=(400,400), background_color='#4f280a',element_justification='center', keep_on_top=True, grab_anywhere=True)
    texto = ['Chequeando imágenes de fichas','Chequeando imágenes de casilleros especiales','Chequeando imágenes de avatares','LISTO PARA JUGAR']
    chequeos=[]
    fichas, especiales, avatares = check_fichas(),check_especiales(),check_avatares()
    chequeos.append(fichas)
    chequeos.append(especiales)
    chequeos.append(avatares)
    i=0
    while True: 
        event, values = v.read(timeout=10) 
        if i < 4:
            v['texto'].update('{}'.format(texto[i]))
            try:
                if str(chequeos[i]) > '0':
                    v['ok'].update('Cuidado, tienes imágenes dañadas') 
                    img2 = crear_error() 
                else:
                    v['ok'].update('Correctas')
            except:
                pass
            i += 1        
            time.sleep(2)
        else: 
            break         
    v.close()
if __name__ == '__main__':
    loading()
