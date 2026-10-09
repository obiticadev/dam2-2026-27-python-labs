"""Programa principal del ejercicio 16.

Importa las tres funciones de textos.py y utilízalas sobre una misma frase de
ejemplo.
"""

from textos import contar_apariciones, contar_vocales, longitud_sin_espacios


palabra = "ADIOOOOOOSsssee y adios se dijo    la cola      "
frase = "Adios caracolaaa"
print(contar_apariciones(frase, palabra))
print(contar_vocales(frase))
print(longitud_sin_espacios(frase))
