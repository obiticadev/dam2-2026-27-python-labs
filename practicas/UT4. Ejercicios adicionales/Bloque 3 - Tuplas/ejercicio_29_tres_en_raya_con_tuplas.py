"""Ejercicio 29: Tres en raya con tuplas.

Nivel: Alto.

Enunciado: Un tablero de tres en raya se representa con una tupla de tres tuplas, una
por fila, con los textos "X", "O" o " " (casilla libre). Define la constante LINEAS, una
tupla con las 8 líneas ganadoras (3 filas, 3 columnas y 2 diagonales), donde cada línea
es una tupla de tres casillas (fila, columna). Escribe:

- ganador(tablero), que recorra las líneas y devuelva "X" u "O" si hay tres iguales en
  una línea (y None si no hay ganador);

- hay_empate(tablero), que devuelva True si no hay ganador y no quedan casillas libres;

- poner_ficha(tablero, fila, columna, ficha), que, como las tuplas son inmutables,
  devuelva un tablero nuevo con la ficha colocada (o el mismo tablero si la casilla
  estaba ocupada);

- y mostrar(tablero), que lo imprima con el formato X|O|X.

Prueba las funciones con un tablero ganador, uno empatado y uno vacío en el que coloques
varias fichas.
"""
