"""Programa principal del ejercicio 15.

Importa a la vez las tres funciones y la constante PI con una única sentencia:

    from geometria import ...

Utiliza todos los elementos importados.
"""
from geometria import area_circulo, area_cuadrado, perimetro_circulo, PI

radio = 5
lado = 11

print(f"Constante PI = {PI}")
print(
    f"El método {area_circulo.__qualname__} con {radio} de radio es igual a {area_circulo(radio):,.2f}")
print(
    f"El método {perimetro_circulo.__qualname__} con {radio} de radio es igual a {perimetro_circulo(radio):,.2f}")
print(
    f"El método {area_cuadrado.__qualname__} con {lado} de lado es igual a {area_cuadrado(lado):,.2f}")
