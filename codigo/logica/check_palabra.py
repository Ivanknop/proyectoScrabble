import pattern.es as pes

def check_jugador(palabra):
    """ recibe una palabra y verifica que sea un verbo, adjetivo o sustantivo,
    retorna True si es asi, o Fale en caso contrario"""

    #podria chequearse con lexicon y las otras listas de palabras de pattern

    pal = pes.parse(palabra).split('/')

    if pal[1] == 'VB':
        return True
    elif pal[1] == 'UH':
        return True
    elif pal[1] == 'JJ':
        return True
    else:
        return False


def check_compu(palabra):
    pass
