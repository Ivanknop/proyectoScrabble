'''ESTA VERSION DEL CODIGO ESTA BASADA EN LA ULTIMA MODIFICACION DE LA ENTREGA
EN LA CUAL SE ESTABLECIERON PAUTAS DISTINTAS,POR PARTE DE LA CATEDRA, PARA LAS DIFERENTE DIFICULTADES
SEGUIREMOS PEMRITIENDO PALABRAS OCN ACENTOS YA QUE ESTABA SOLUCIONADO EE PROBLEMA
PERO ESTA VEZ CHEQUEARA LA PALABRA (EN EL MODULO check_jugador()) TENIENDO ENCUENTA LA DIFICULTAD NE LA QUE SE ESTE JUGANDO'''


import pattern.es as pes
from pattern.es import verbs, tag, spelling, lexicon
import itertools as it

def posibles_palabras (palabra):
    '''por cada vocal, que tenga la palabra, genera una posibilidad con Tilde
    debido a que nuestro programa solo contiene letras sin tilde
    pero pattern tiene palabras ocn tilde, por ejemplo el juego logicamente ingresa pajaro, sin tilde pero en
    pattern esta se encuentra ocn tilde. aqui generamos esa lista con posible opciones onc tilde para que pattern las encunetre
    en su diccionario de palabras'''

    lisPal = []
    #siempre la primer palabra sera la ingresada por le ugador
    lisPal.append(palabra)
    vocales = {'a':'á', 'e':'é', 'i':'í', 'o':'ó', 'u':'ú'}

    #encontre una forma pythonica de obtener los indices
    pos = [idx for idx, x in enumerate(palabra) if x in vocales.keys()]

    # for i in range(len(palabra)):
    #     if palabra[i] in vocales.keys():
    #
    #         pos.append(palabra.index(palabra[i]))


     #le pongo tilde a esas vocales, y agrego la palabra
    for it in range(len(pos)):
        pal_temp = ''

        for it2 in range(len(palabra)):

            if it2 != pos[it]:

                pal_temp += palabra[it2]
            else:

                pal_temp += vocales[palabra[pos[it]]]

        lisPal.append(pal_temp)


    return lisPal


def clasificar(palabra):
    print(tag(palabra, tokenize=True, encoding='utf-8', tagset='UNIVERSAL'))
    print(tag(palabra, tokenize=True, encoding='utf-8'))
    print()


def es_palabra(palabra):
    ''' este modulo evalua si la palabra recibida existe en los diccionarios de PATTERN.ES'''
    ok = True
    if palabra:
        if not palabra.lower() in verbs:
            if not palabra.lower() in spelling:
                if (not (palabra.lower() in lexicon) and not (palabra.upper() in lexicon) and not (
                        palabra.capitalize() in lexicon)):
                        ok = False
                else:
                    print('La encontró en lexicon')
                    clasificar(palabra)
            else:
                print('La encontró en spelling')
                clasificar(palabra)
        else:
            print('La encontró en verbs')
            clasificar(palabra)
    return ok


def check_jugador(palabra, dificultad ='facil'):
    """ recibe una palabra y verifica que sea un verbo, adjetivo o sustantivo,
    retorna True si es asi, o Fale en caso contrario.
    este modulo asignara por defecto la dificultad ne FACIL si no es indicada"""

    if len(palabra) >= 2:
        global TIPO
        posibles = posibles_palabras(palabra)
        ok = False
        cont = 0
        #en cuanto encunetre una opcion que de 'True' dejara de comprobar e insertara esa
        while not ok and cont < len(posibles):
            pal = ''

            pal = pes.parse(posibles[cont]).split('/')
            if es_palabra(posibles[cont]) and dificultad == 'facil':

                if pal[1] in TIPO['adj']:
                    ok =True
                elif pal[1] in TIPO['sus']:
                    ok= True
                elif pal[1] in TIPO['verb']:
                   ok= True
                else:
                    ok= False
            elif es_palabra(posibles[cont]) and (dificultad == 'medio' or  dificultad == 'dificil'):
                if pal[1] in TIPO['adj']:
                    ok =True
                elif pal[1] in TIPO['verb']:
                   ok= True
                else:
                    ok= False
            else:
                ok = False

#            print("se chequeo {} el contador es {} y ok esta en {}".format(pal,cont,ok))
            cont += 1
    else:
        return False
    return ok

def check_compu(atril_pc, tablero):
    fichas_pc = atril_pc.ver_atril()
    letras = ''
    for ficha in fichas_pc:
        letras += list(ficha.keys())[0]
    palabras = set()
    for i in range(2, len(letras)+1):
        palabras.update(map(''.join, it.permutations(letras, i)))
    posibilidades = {}
    for pal in palabras:
        if check_jugador(pal),tablero.getNivel():
            fichas_pal = []
            for letra in pal:
                for ficha in fichas_pc:
                    if list(ficha.keys())[0] == letra:
                        fichas_pal.append(ficha)
                        break
            busqueda = tablero.buscarEspacio(fichas_pal)
            if busqueda['coordenada'] != -1:
                busqueda['fichas'] = fichas_pal
                posibilidades[pal] = busqueda
    for clave, valor in posibilidades.items():
        print(clave, ':', valor['interes'])
    print('')
    if len(posibilidades) > 0:
        mejor_opcion = max(posibilidades, key = lambda d: posibilidades[d]['interes'])
        print('La mejor opcion es: ' + mejor_opcion + '. En la coordenada ' + str(posibilidades[mejor_opcion]['coordenada'][0]) + ', ' + str(posibilidades[mejor_opcion]['coordenada'][1]))
        return posibilidades[mejor_opcion]
    return posibilidades



    #Iterar "palabras" por check_palabra. Si es válida, guardar en un diccionario
    #la palabra y la coordenada (si hubiese espacio) en la que obtendría mayor
    #puntaje. Luego, quedarse con la palabra que haya arrojado mayor puntaje.
    #Observar que una palabra de 2 letras puede dar mayor puntaje si, por ejemplo,
    #cabe en una parte del tablero muy beneficiosa en la que una de 4 letras no.



'''TIPO sera una varible global que nos permite chequiar que la palabra a ingresar, este dentor
de las clasificaciones permitidas en el juego  adj = adjetivos, sus= sustantivo, verb = verbos
las clasificiaciones estan tomadas dle modulo pattern, pero la construccio nde este modulo
facilita su comprovacion
'''
TIPO= {'adj':["AO", "JJ","AQ","DI","DT"],
         'sus':["NC", "NN", "NCS","NCP", "NNS","NP", "NNP","W"],
          'verb':[ "VAG", "VBG", "VAI","VAN", "MD", "VAS" , "VMG" , "VMI", "VB", "VMM" ,"VMN" , "VMP", "VBN","VMS","VSG",  "VSI","VSN", "VSP","VSS"  ]
          }


#print(check_jugador('abaco'))
