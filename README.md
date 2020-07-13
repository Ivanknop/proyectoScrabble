ScrabbleAR es un proyecto realizado para el Seminario de Lenguaje Python.

Fue realizado por: 

Diego Vilardebó - https://github.com/elrecursante -

Enzo Diaz - https://github.com/enzodiaz25 -

Ivan Knopoff - https://github.com/Ivanknop - ivan.knopoff@gmail.com 



Simula una aplicación donde un usuario/jugador debe enfrentarse a la computadora. El objetivo del juego es obtener la mayor cantidad de puntos posibles colocando las palabras en horizontal o vertical; pero sin cruzarse ninguna palabra entre sí. Pueden escogerse entre tres dificultades -Fácil, Medio, Difícil- o configurar directamente la partida y la dificultad.

Se requiere de las librerías:

PySIMPLEGUI

PIL

Pattern 3.6


Se recomienda compilar en Python 3.6.10 o anterior por un problema entre el mismo y la librería Pattern.


Dinámica del juego:
1) Se determina al azar quién empieza.
2) El jugador selecciona la mejor combinación de palabras posibles y la inserta en el tablero. En este hay casilleros ordinarios y otros especiales que alteran el puntaje final de la palabra insertada. En el caso del computador, la selección de la palabra y del lugar del tablero está determinado por el algoritmo de dificultad.
3) Una vez seleccionadas las letras se corrobora que sea una palabra válida. 
4) En caso afirmativo, se decide dónde insertar y la orientación. Si hay lugar -es decir que la palabra no termina fuera del tablero ni se cruza con alguna letra de otra palabra-, se inserta y se incrementa el puntaje total.
5) En caso negativo, se debe seleccionar otra combinación de letras.
6) El Usuario/Jugador dispone de 3 (tres) cambios de sus fichas antes de tener que dar por terminada la partida.
