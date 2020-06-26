import PySimpleGUI as sg
import os

class Visor():
    '''El objeto Visor es un widget implementado con el fin de generar un selector de AVATAR para el
    juego. Pero es más que eso, este widget no está implementado en la libreria PySimpleGui.
    Visor permite generar un widget del tipo galeria para visualizar imagenes con solohacer una instancia de este objeto
    aun hay que retocarlo para que sea mpas generico. pero la idea es esa.
    '''
    def __init__(self, directorio):
        #Procesa varios datos a través del directorio de las imágenes
        infoImg = self._ruta_imagenes(directorio)
        self._directorio = directorio
        #... como una lista con la ruta de cada imágen
        self._imagenes = infoImg['imagenes']
        #... y la cantidad total de avatares
        self._cantImagenes = infoImg['cant_imagenes']
        #El avatar por defecto será el primero de la lista de imagenes (índice 0)
        self._i=0

    def  _ruta_imagenes(self, directorio):
        #Si el directorio no existe, la advierte y cierra el programa
        if not directorio:
            sg.popup_cancel('Cancelando')
            raise SystemExit()

        #Lista todos los archivos del directorio
        archivo = os.listdir(directorio)

        #Obtiene las imagenes que haya en el directorio
        imgTipos = (".png", ".jpg", "jpeg", ".tiff", ".bmp")
        imagenes = [f for f in archivo if os.path.isfile(
            os.path.join(directorio, f)) and f.lower().endswith(imgTipos)]

        cant_imagenes = len(imagenes)
        #Si no encontró ninguna imágen, termina la ejecución del juego
        if cant_imagenes == 0:
            sg.popup('no hay avatares')
            raise SystemExit()

        return {'imagenes': imagenes, 'cant_imagenes': cant_imagenes}

    def controles(self, event, visor):
        '''esta funcion e encarga de avanzar o retroceder en la lista de imagenes del directorio
        que luego eran visualizadas
        al mismo tiempo returna la ruta de la imagen que esta actualmente en le visor'''
        #El indice self._i se inicializa en 0 al instanciar el objeto
        if event == '>>>':
            self._i += 1
            if self._i >= self._cantImagenes:
                self._i -= self._cantImagenes
            avatar = os.path.join(self._directorio, self._imagenes[self._i])
        elif event == '<<<':
            self._i-= 1
            if self._i < 0:
                self._i = self._cantImagenes + self._i
            avatar =  os.path.join(self._directorio, self._imagenes[self._i])
        else:
            avatar =  os.path.join(self._directorio, self._imagenes[self._i])
        visor.Update(filename=avatar)
        return avatar

    def getAvatarLayout(self):
        #Retorna el layout del visor
        avatar = os.path.join(self._directorio, self._imagenes[0])
        galeria = [[sg.Image(filename=avatar,key ='avatarVisor')],
                   [sg.Button('<<<', size=(8, 2), button_color=('black', '#f75404')), sg.Button('>>>', size=(8, 2), button_color=('black', '#f75404'))],
            ]
        return galeria

    def getAvatar(self):
        #Devuelve la posición, en la lista de imagenes, del avatar seleccionado
        #actualmente
        return self._i

    def getActualRuta(self):
        return os.path.join(self._directorio, self._imagenes[self._i])


# if __name__ == '__main__':
#
#
#
#     v = Visor(directorio)
#     lay = [[sg.Column(v.galAvatar())],]
#     win=sg.Window('asd',layout=lay).Finalize()
#
#     while True:
#
#         e , va = win.read()
#         if e in ('<<<','>>>'):
#              v.controles(e, win.FindElement('avatarVisor'))