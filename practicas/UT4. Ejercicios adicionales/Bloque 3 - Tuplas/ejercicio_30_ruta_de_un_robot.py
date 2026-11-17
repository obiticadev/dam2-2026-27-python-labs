"""Ejercicio 30: Ruta de un robot.

Nivel: Alto.

Enunciado: Un robot parte de la posición (0, 0) y sigue una ruta formada por una lista
de tuplas (direccion, pasos), por ejemplo [("N", 3), ("E", 4), ("S", 1), ("O", 6), ("S",
2)]. Define un diccionario constante MOVIMIENTOS que asocie cada dirección con el
desplazamiento de un paso como tupla (dx, dy) ("N": (0, 1), "S": (0, -1), "E": (1, 0),
"O": (-1, 0)). Escribe:

- ejecutar_ruta(ruta), que devuelva una tupla (posicion_final, trayecto), donde trayecto
  es la lista de todas las posiciones por las que pasa el robot tras cada tramo
  (empezando en el origen); las direcciones desconocidas se ignoran;

- distancia_manhattan(posicion), que devuelva abs(x) + abs(y);

- y punto_mas_alejado(trayecto), que devuelva la posición del trayecto más lejana al
  origen (usa max() con key).

Prueba el programa con la ruta de ejemplo y con una ruta que vuelva al origen ([("N",
2), ("E", 2), ("S", 2), ("O", 2)]).
"""
