import pattern.es as pes
from pattern.es import verbs, tag, spelling, lexicon



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
        #podria chequearse con lexicon y las otras listas de palabras de pattern
        if es_palabra(palabra):
            pal = pes.parse(palabra).split('/')

            if pal[1] in TIPO['adj']:
                return True
            elif pal[1] in TIPO['sus']:
                return True
            elif pal[1] in TIPO['verb']:
                return True
            else:
                return False
        return False
    else:
        return False

def check_compu(palabra):
    pass
#TIPO sera una varible global que nos permite chequiar que la palabra a ingresar, este dentor
#de las clasificaciones permitidas en el juego  adj = adjetivos, sus= sustantivo, verb = verbos

TIPO= {'adj':["AO", "JJ","AQ","DI","DT"],
         'sus':["NC", "NN", "NCS","NCP", "NNS","NP", "NNP","W"],
          'verb':[ "VAG", "VBG", "VAI","VAN", "MD", "VAS" , "VMG" , "VMI", "VB", "VMM" ,"VMN" , "VMP", "VBN","VMS","VSG",  "VSI","VSN", "VSP","VSS"  ]
          }

