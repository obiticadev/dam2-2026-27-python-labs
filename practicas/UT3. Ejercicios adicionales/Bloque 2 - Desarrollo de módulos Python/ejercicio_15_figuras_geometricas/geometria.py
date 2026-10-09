"""Ejercicio 15: Módulo de figuras geométricas.

Crea una constante PI y las funciones area_circulo(radio),
perimetro_circulo(radio) y area_cuadrado(lado). Añade un bloque de pruebas
protegido con if __name__ == "__main__":.
"""
import math
PI = math.pi


def area_circulo(radio: float) -> float:
    return PI * radio ** 2


def perimetro_circulo(radio: float) -> float:
    return 2 * PI * radio


def area_cuadrado(lado: float) -> float:
    return lado ** 2


if __name__ == "__main__":
    radio = 20
    lado = 10
    print(
        f"El método {area_circulo.__qualname__} con {radio} de radio es igual a {area_circulo(radio):,.2f}")
    print(
        f"El método {perimetro_circulo.__qualname__} con {radio} de radio es igual a {perimetro_circulo(radio):,.2f}")
    print(
        f"El método {area_cuadrado.__qualname__} con {lado} de lado es igual a {area_cuadrado(lado):,.2f}")
