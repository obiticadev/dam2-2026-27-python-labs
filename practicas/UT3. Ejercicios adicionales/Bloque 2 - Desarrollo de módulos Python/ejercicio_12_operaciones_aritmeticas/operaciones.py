"""Ejercicio 12: Módulo de operaciones aritméticas básicas.

Crea las funciones sumar(a, b), restar(a, b), multiplicar(a, b) y
dividir(a, b). La última debe controlar con try/except la división entre cero y
devolver None en ese caso. Añade un bloque if __name__ == "__main__": que
compruebe las cuatro funciones.
"""


def sumar(a: float, b: float) -> float:
    return a + b


def restar(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float | None:
    try:
        if b == 0:
            raise ZeroDivisionError
    except ZeroDivisionError:
        return None
    return a / b


if __name__ == "__main__":
    a = 10
    b = 3
    c = 0
    print(sumar(a, b))
    print(restar(a, b))
    print(multiplicar(a, b))
    print(dividir(a, b))
    print(dividir(a, c))
