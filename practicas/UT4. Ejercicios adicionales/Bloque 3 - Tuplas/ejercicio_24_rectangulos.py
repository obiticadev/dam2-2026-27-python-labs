"""Ejercicio 24: Rectángulos.

Nivel: Medio.

Enunciado: Un rectángulo se representa con una tupla (x, y, ancho, alto), donde (x, y)
es su esquina inferior izquierda. Escribe:

- area(rectangulo) y perimetro(rectangulo);

- contiene_punto(rectangulo, punto), que reciba el punto como tupla (px, py) y devuelva
  True si está dentro del rectángulo (incluidos los lados izquierdo e inferior, pero no
  el derecho ni el superior);

- rectangulo_mayor(lista_rectangulos), que devuelva el de mayor área (usa max() con
  key=area); y se_solapan(r1, r2), que devuelva True si los dos rectángulos comparten
  alguna zona (no basta con que se toquen en un lado).

Prueba las funciones con rectangulos = [(0, 0, 4, 3), (2, 1, 5, 5), (10, 10, 2, 2)].
"""
