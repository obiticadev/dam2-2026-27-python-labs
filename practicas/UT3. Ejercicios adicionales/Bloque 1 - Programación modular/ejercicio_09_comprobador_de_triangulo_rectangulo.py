"""Ejercicio 9: Comprobador de triángulo rectángulo.

Codifica una función es_triangulo_rectangulo(a, b, c) que, a partir de las
longitudes de los tres lados de un triángulo, determine si es rectángulo
aplicando el teorema de Pitágoras. Usa el módulo math.
"""
import math


def es_triangulo_rectangulo(a: float, b: float, c: float) -> bool:
    return True if (math.pow(a, 2)+math.pow(b, 2) == math.pow(c, 2)) else False


while True:
    while True:
        try:
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            break
        except ValueError as e:
            print(e)

    print(es_triangulo_rectangulo(a, b, c))
