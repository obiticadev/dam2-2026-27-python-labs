"""Ejercicio 4: Contador de consonantes.

Codifica una función contar_consonantes(palabra) que recorra una palabra letra
a letra, con un bucle for, y devuelva cuántas consonantes contiene.
"""
import re


def contar_consonantes(palabra: str) -> int:
    patron = r"[^aeiouáéíóúü]"
    for letra in palabra:
        if letra.isalpha() and re.search(patron, letra, re.IGNORECASE):
            contador += 1
    return contador


palabra = input("Introduce una palabra: ")
print(f"{palabra.upper} contine {contar_consonantes(palabra)} consonantes")
