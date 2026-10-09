"""Ejercicio 17: Módulo de estadística sencilla.

Crea las funciones calcular_media(a, b, c), calcular_maximo(a, b, c), usando
max(), y calcular_minimo(a, b, c), usando min(). Añade un bloque de pruebas
protegido con if __name__ == "__main__":.
"""

import statistics


def calcular_media(a: float, b: float, c: float) -> float:
    return statistics.mean([a, b, c])


def calcular_maximo(a: float, b: float, c: float) -> float:
    return max(a, b, c)


def calcular_minimo(a: float, b: float, c: float) -> float:
    return min(a, b, c)


if __name__ == "__main__":
    a = 10
    b = 20
    c = 30
    print(calcular_media(a, b, c))
    print(calcular_maximo(a, b, c))
    print(calcular_minimo(a, b, c))
