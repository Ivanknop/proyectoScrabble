import random #es sólo para la carga random de la bolsa de fichas
class Atril():
    def __init__ (self,bolsa_fichas,cant_fichas):
        self._cant_Fichas = cant_fichas
        self._lista_Fichas = []
        for i in range(cant_fichas):
            self._lista_Fichas.append(bolsa_fichas[0])
            bolsa_fichas.remove(bolsa_fichas[0])

    #Devuelve la ficha seleccionada. Debe modificarse según se implemente la interfaz
    def get_ficha(self, pos): 
        return self._lista_Fichas[pos]
    
    #Solamente evalúa si hay elementos en bolsa_fichas. Hay que analizar al llamarlo la 'cantidad de veces disponibles'
    def cambiar_fichas (self,bolsa_fichas,cant_fichas):
        self._cant_Fichas = 0
        self._lista_Fichas = []
        while bolsa_fichas and self._cant_Fichas < cant_fichas:
            self._lista_Fichas.append(bolsa_fichas[0])
            bolsa_fichas.remove(bolsa_fichas[0])
            self._cant_Fichas += 1

    #retorna la cantidad de elementos en el atril
    def ver_atril(self):
        return self._lista_Fichas
    
    def get_cant_fichas(self):
        return self._cant_Fichas

#Esto es para probar
FICHAS = 3 #Creo que deberían ser 7 en el juego original
b_fichas = []
for i in range(10): #Simple relleno para después meter las fichas posta
    b_fichas.append({'Letra':'A','Puntaje':i})
    b_fichas.append({'Letra':'B','Puntaje':i})
random.shuffle(b_fichas)  
print('Bolsa de Fichas: ', b_fichas)  
print('')
jugador = Atril(b_fichas, FICHAS)
print ('Jugador: ', jugador.ver_atril())
print('')
print (b_fichas)
print('')
jugador.cambiar_fichas(b_fichas,FICHAS)
print ('Jugador: ',jugador.ver_atril())
print('')
print ('Bolsa de Fichas: ', b_fichas)
print('')
print (jugador.get_cant_fichas())
print('')