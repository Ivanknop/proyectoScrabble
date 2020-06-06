import random


def especial(fila, col,nivel):
    ''' esta funci{on genera casilleros especiales, segun el nivel
    teniendo en cuenta la cantidad de columnas y filas, y la dificultad dle mismo
    y siempre controla que tenga cierta cantidad de casilleros especiales'''



    if nivel == 'facil':
        esp = ['*rest', '*sum']
        minEsp= 10
    elif nivel == 'medio':
        esp = ['*rest', '*sum', '*mult', '*div' ]
        minEsp = 7
    elif nivel == 'dificil':
        esp = ['*rest', '*sum', '*mult', '*0', '*div']
        minEsp = 7
    else:
        esp = []



    especiales = {}
    # minok = False
    # while not minok:
    for row in range(fila):
        for col in range(col):
            if random.randint(0, 100) > 10:
                pass
            else:
                # aca asigno el casillero especial
                l = [str(row), ', ', str(col)]
                c = ''.join(l)

                random.shuffle(esp)
                especiales[c] = esp[0]

        # controlo el minimo de casilleros
        # print(especiales)
        # print(len(especiales))
        # if len(especiales) >= minEsp:
        #     minok = True

    return especiales

def nivel_facil():
    conf = {
        'nivel':'facil',
        'filas':20,
        'columnas':20,
        'especiales':{},

        'timepo': 25, #minutos
        'cant_fichas': {'A':11, 'E':11, 'O':8, 'S':7, 'I':6,'U': 6, 'N': 5, 'L': 4, 'R': 4, 'T': 4,'C': 4, 'D': 4, 'G': 2, 'M': 3, 'B': 3,'P': 2, 'F': 2, 'H': 2, 'V': 2, 'Y': 1,'J': 2, 'K': 1, 'Ñ': 1, 'Q': 1, 'W': 1, 'X': 1, 'Z': 1 },

         #  dic el indice indica le puntaje y lo valores son las letras que itenen ese puntaje
        # tienen mayor puntaje que otros niveles
         'puntaje_ficha' : {
        5: ['A', 'E', 'O', 'S', 'I', 'U', 'N', 'L', 'R', 'T'],
        2: ['C', 'D', 'G'],
        8: ['M', 'B', 'P'],
        4: ['F', 'H', 'V', 'Y'],
        6: ['J'],
        9: ['K', 'Ñ', 'Q', 'W', 'X'],
        10: ['Z']
    }
    }
    conf['especiales']=especial(conf['filas'], conf['columnas'],conf['nivel'])
    return conf


def nivel_medio():
    # tiene menor cantidad de vocales
    # tiene menos punto las letras
    #el tablero sera un poco mas chico
    #y menor tiempo de juego
    conf = {
        'nivel': 'medio',
        'filas':15,
        'columnas':15,
        'especiales': {},
        'timepo': 20, #minutos
        # el indice es la letra y e lvalor la cantidad de fichas de esa letra

        'cant_fichas' : {
        'A':9, 'E':9, 'O' :8, 'S' :7, 'I' :6,
        'U':6, 'N':5, 'L':4, 'R':4, 'T':4,
        'C':4, 'D':4, 'G' :2, 'M' :3, 'B' :3,
        'P' :2, 'F' :2, 'H' :2, 'V':2, 'Y' :1,
        'J':2, 'K' :1, 'Ñ' :1, 'Q' :1, 'W' :1, 'X' :1, 'Z' :1
    },

         #  dic el indice indica le puntaje y lo valores son las letras que itenen ese puntaje
         'puntaje_ficha' : {
        1: ['A', 'E', 'O', 'S', 'I', 'U', 'N', 'L', 'R', 'T'],
        2: ['C', 'D', 'G'],
        3: ['M', 'B', 'P'],
        4: ['F', 'H', 'V', 'Y'],
        6: ['J'],
        8: ['K', 'Ñ', 'Q', 'W', 'X'],
        10: ['Z']
    }
    }
    conf['especiales'] = especial(conf['filas'], conf['columnas'],conf['nivel'])
    return conf


def nivel_dificil():
    # tiene menor cantidad de vocales
    # misma puntuacion que en el nivel medio
    # el tablero sera igual al nivel medio
    # y menor tiempo de juego
    # tendra mas casilleros que restan puntos
    conf = {
        'nivel': 'dificil',
        'filas': 10,
        'columnas': 10,
        'especiales': {},  # ver de armarl ode forma random
        'timepo': 15,  # minutos
        # el indice es la letra y e lvalor la cantidad de fichas de esa letra

        'cant_fichas': {
            'A':9, 'E':9, 'O' :8, 'S' :7, 'I' :6,
        'U':6, 'N':5, 'L':4, 'R':4, 'T':4,
        'C':4, 'D':4, 'G' :2, 'M' :3, 'B' :3,
        'P' :2, 'F' :2, 'H' :2, 'V':2, 'Y' :1,
        'J':2, 'K' :1, 'Ñ' :1, 'Q' :1, 'W' :1, 'X' :1, 'Z' :1
        },

        #  dic el indice indica le puntaje y lo valores son las letras que itenen ese puntaje
        'puntaje_ficha': {
            1: ['A', 'E', 'O', 'S', 'I', 'U', 'N', 'L', 'R', 'T'],
            1: ['C', 'D', 'G'],
            3: ['M', 'B', 'P'],
            4: ['F', 'H', 'V', 'Y'],
            6: ['J'],
            8: ['K', 'Ñ', 'Q', 'W', 'X'],
            10: ['Z']
        }
    }
    conf['especiales'] = especial(conf['filas'], conf['columnas'],conf['nivel'])
    return conf
    
