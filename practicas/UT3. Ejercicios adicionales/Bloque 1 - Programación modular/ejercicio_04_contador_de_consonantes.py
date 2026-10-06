"""Ejercicio 4: Contador de consonantes.

Codifica una función contar_consonantes(palabra) que recorra una palabra letra
a letra, con un bucle for, y devuelva cuántas consonantes contiene.
"""
import re


def contar_consonantes(palabra: str):
    for char in palabra:
        re.search(r"[^aeiou]", char)
