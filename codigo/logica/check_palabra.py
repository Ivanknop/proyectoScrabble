import pattern.es as pes
from pattern.es import verbs, tag, spelling, lexicon

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


def check_jugador(palabra):
    """ recibe una palabra y verifica que sea un verbo, adjetivo o sustantivo,
    retorna True si es asi, o Fale en caso contrario"""
    if len(palabra) >= 2:

        global TIPO
        posibles = posibles_palabras(palabra)
        ok = False
        cont = 0
        #en cuanto encunetre una opcion que de 'True' dejara de comprobar e insertara esa
        while not ok and cont < len(posibles):
            pal=''
            if es_palabra(posibles[cont]):
                pal = pes.parse(posibles[cont]).split('/')

                if pal[1] in TIPO['adj']:
                    ok =True
                elif pal[1] in TIPO['sus']:
                    ok= True
                elif pal[1] in TIPO['verb']:
                   ok= True
                else:
                    ok= False
            else:

                ok = False

            print("se chequeo {} el contador es {} y ok esta en {}".format(pal,cont,ok))
            cont += 1
    else:
        return False
    return ok

def check_compu(palabra):
    pass



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
