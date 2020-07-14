from codigo.interfaz import interfaz_inicial
from codigo.logica import juego

def main():
    '''Ejecuta la interfaza principal y, si se ingresaron datos
    para el jugador, inicia el juego. Respectivamente, si la primera
    retorna un jugador vacío (por ejemplo, si se cierra la ventana sin
    hacer nada), la segunda parte no se ejecuta.'''
    datos_jugador, cargar = interfaz_inicial.lazo_principal()
    if (datos_jugador.getNombre() != ''):
        juego.lazo_principal(datos_jugador, cargar)

if __name__ == '__main__':
    main()