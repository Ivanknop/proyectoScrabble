import PySimpleGUI as sg
import os

directorio = os.path.join('..','Scrabble','media','media_ii','avatars', '')  #  sg.popup_get_folder('Image folder to open', default_path='')

class Visor():

    def __init__(self,directorio):
        infoImg = self.__ruta_imagenes(directorio)
        self.__directorio = directorio
        self.__imagenes = infoImg[0]
        self.__cantImagenes =infoImg[1]
        self.__i=0



    def  __ruta_imagenes(self,directorio):

        if not directorio:
            sg.popup_cancel('Cancelling')
            raise SystemExit()


        imgTipos = (".png", ".jpg", "jpeg", ".tiff", ".bmp")

        # listo todos lso archivos del directorio
        archivo = os.listdir(directorio)

        # solo me quedo ocn las imagenes uqe alla en el directorio
        imagenes = [f for f in archivo if os.path.isfile(
            os.path.join(directorio, f)) and f.lower().endswith(imgTipos)]

        cant_imagenes = len(imagenes)
        if cant_imagenes == 0:
            sg.popup('no hay avatares')

            raise SystemExit()

        del archivo

        return (imagenes,cant_imagenes)



    def controles(self,event,visor):
        '''esta funcion e encarga de avanzar o retroceder en la lista de imagenes del directorio
        que luego eran visualizadas
        al mismo tiempo returna la ruta de la imagen que esta actualmente en le visor'''
        #el indice self.__i se inicializa en 0 al instanciar el objeto

        if event == '>>>':
            self.__i += 1
            if self.__i >= self.__cantImagenes:
                self.__i -= self.__cantImagenes
            avatar = os.path.join(self.__directorio, self.__imagenes[self.__i])
        elif event == '<<<':
            self.__i-= 1
            if self.__i < 0:
                self.__i = self.__cantImagenes + self.__i
            avatar =  os.path.join(self.__directorio, self.__imagenes[self.__i])

        else:
            avatar =  os.path.join(self.__directorio, self.__imagenes[self.__i])

        visor.Update(filename=avatar)

        return avatar




    def galAvatar(self):


        avatar = os.path.join(self.__directorio, self.__imagenes[0])

        galeria = [[sg.Image(filename=avatar,key ='avatarVisor')],
                   [sg.Button('<<<', size=(8, 2)), sg.Button('>>>', size=(8, 2))],
            ]

        #return [[sg.Column(galeria, visible=True,key='galeria')]]
        return galeria



#
# v = Visor(directorio)
# lay = [[sg.Column(v.galAvatar())],]
# win=sg.Window('asd',layout=lay).Finalize()
#
# while True:
#
#     e , va = win.read()
#     if e in ('<<<','>>>'):
#          v.controles(e, win.FindElement('avatarVisor'))