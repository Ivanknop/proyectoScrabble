import interfaz_inicial
import juego

def main():
    datos_jugador = interfaz_inicial.lazo_principal()
    if (datos_jugador.getNombre() != ''):
        juego.lazo_principal(datos_jugador)

if __name__ == '__main__':
    main()