"""Ejercicio 16: Módulo de utilidades de texto.

Crea estas funciones:

- contar_apariciones(frase, palabra), usando .count().
- contar_vocales(frase), recorriendo la frase con un bucle for.
- longitud_sin_espacios(frase), contando con for los caracteres no espaciales.

Añade un bloque de pruebas protegido con if __name__ == "__main__":.
"""

import re


def contar_apariciones(frase: str, palabra: str) -> int:
    return frase.count(palabra)


def contar_vocales(frase: str) -> int:
    return len(re.findall(r"[aeiou]", frase, flags=re.IGNORECASE))


def longitud_sin_espacios(frase: str) -> int:
    num = 0
    for i in frase.strip():
        if i != " ":
            num += 1
    return num


if __name__ == "__main__":
    palabra = "Hola y adios se dijo    la cola      "
    frase = "Hola caracola"
    print(contar_apariciones(frase, palabra))
    print(contar_vocales(frase))
    print(longitud_sin_espacios(frase))
