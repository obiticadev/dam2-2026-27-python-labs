"""Ejercicio 21: Colores RGB.

Nivel: Básico.

Enunciado: Un color se representa con una tupla (rojo, verde, azul), con valores enteros
de 0 a 255. Define las constantes ROJO = (255, 0, 0), VERDE = (0, 255, 0) y NEGRO = (0,
0, 0). Escribe:

- es_color_valido(color), que devuelva True si la tupla tiene exactamente tres
  componentes y todas están entre 0 y 255;

- invertir_color(color), que devuelva el color complementario (255 - r, 255 - g, 255 -
  b);

- a_gris(color), que devuelva el gris equivalente, es decir, una tupla con la media de
  los tres componentes (división entera) repetida tres veces;

- y mezclar(color1, color2), que devuelva el color formado por la media de cada
  componente. Desempaqueta los colores en variables para hacer los cálculos. Prueba las
  funciones con las constantes y con una tupla inválida como (300, 0, 0).
"""
