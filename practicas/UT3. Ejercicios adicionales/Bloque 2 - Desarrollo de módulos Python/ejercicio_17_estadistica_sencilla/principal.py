"""Programa principal del ejercicio 17.

Importa las tres funciones de estadistica.py y utilízalas sobre tres notas.
"""

from estadistica import calcular_minimo, calcular_maximo, calcular_media

a = 50
b = 60
c = 70

print(calcular_media(a, b, c))
print(calcular_maximo(a, b, c))
print(calcular_minimo(a, b, c))
