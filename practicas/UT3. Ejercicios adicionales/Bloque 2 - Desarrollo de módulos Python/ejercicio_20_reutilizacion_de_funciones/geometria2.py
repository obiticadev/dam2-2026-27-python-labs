"""Ejercicio 20: Módulo con reutilización interna de funciones.

Crea las funciones area_rectangulo(base, altura),
perimetro_rectangulo(base, altura), area_cuadrado(lado), que debe reutilizar
area_rectangulo, y perimetro_cuadrado(lado), que debe reutilizar
perimetro_rectangulo. Añade un bloque de pruebas protegido con
if __name__ == "__main__":.
"""


def area_rectangulo(base, altura):
    return base * altura


def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)


def area_cuadrado(lado):
    return area_rectangulo(lado, lado)


def perimetro_cuadrado(lado):
    return perimetro_rectangulo(lado, lado)


if __name__ == "__main__":
    print(area_rectangulo(5, 3))
    print(perimetro_rectangulo(5, 3))
    print(area_cuadrado(4))
    print(perimetro_cuadrado(4))
