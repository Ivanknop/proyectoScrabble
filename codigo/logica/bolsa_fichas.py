from codigo.logica.configuracion import *



def crear_bolsa(cant, puntos):
    ''' esta funcion returna una bolsa de fichas (una lista, donde cada ficha
    es un diccionario' donde la clave es la letra y el valor su puntaje)
    recibe la cantidad y los puntos segun el nivel, el nivel no se determina en este modulo'''
    bolsa = []

    for l in cant:

        ficha = {}
        puntae = 0
        ok = False
        k = 1
        while not ok:
            if k in puntos:
                if l in puntos[k]:
                    #aca armo la ficha
                    puntaje = k
                    ficha[l.lower()] = puntaje
                    ok = True
                else:
                    k += 1
            else:
                k += 1
        #aca la agrego la cantidad de veces especificada segun la dificultad, a la bolsa
        for f in range(cant[l.upper()]):
            bolsa.append(ficha)







    return bolsa



""" ejemplo de su uso
conf = nivel_dificil()

bolsa_fichas = crear_bolsa(conf['cant_fichas'],conf['puntaje_ficha'])
print(bolsa_fichas)"""
