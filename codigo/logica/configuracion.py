

def nivel_facil():
    conf = {
        'nivel':'facil',
        'filas':20,
        'columnas':20,
        'especiales': {'10, 5': '*rojo',
                     '4, 11': '*verde',
                     '20, 5': '*rojo',
                     '14, 5': '*verde',
                     '14, 15': '*verde'}, #ver de armarl ode forma random
        'timepo': 20, #minutos
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
        'especiales': {'10, 5': '*rojo',
                     '4, 11': '*verde',
                     '9, 5': '*rojo',
                     '14, 5': '*verde',
                     '9, 9': '*verde'}, #ver de armarl ode forma random
        'timepo': 15, #minutos
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
        'especiales': {'10, 5': '*rojo',
                       '4, 11': '*rojo',
                       '5, 10': '*rojo',
                       '14, 5': '*rojo',
                       '14, 14': '*verde'},  # ver de armarl ode forma random
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
            2: ['C', 'D', 'G'],
            3: ['M', 'B', 'P'],
            4: ['F', 'H', 'V', 'Y'],
            6: ['J'],
            8: ['K', 'Ñ', 'Q', 'W', 'X'],
            10: ['Z']
        }
    }
    return conf
