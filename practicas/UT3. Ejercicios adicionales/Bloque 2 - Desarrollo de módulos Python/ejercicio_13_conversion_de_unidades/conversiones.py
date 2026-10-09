"""Ejercicio 13: Módulo de conversión de unidades.

Crea las funciones metros_a_pies(metros), pies_a_metros(pies), que realiza la
conversión inversa, y kilometros_a_millas(kilometros). Añade un bloque de
pruebas protegido con if __name__ == "__main__": que compruebe las tres.
"""
METROS_PIES = 3.28084
PIES_METROS = 0.3048
KILOMETROS_MILLAS = 0.621371


def metros_a_pies(metros: float) -> float:
    return metros * METROS_PIES


def pies_a_metros(pies: float) -> float:
    return pies * PIES_METROS


def kilometros_a_millas(kilometros: float) -> float:
    return kilometros * KILOMETROS_MILLAS


if __name__ == "__main__":
    A = 100
    print(f"{A} metros a pies son {metros_a_pies(A):+,.2f} pies")
    print(f"{A} pies a metros son {pies_a_metros(A):_.2f} metros")
    print(f"{A} kilómetros a millas son {kilometros_a_millas(A):,.2f} millas")
