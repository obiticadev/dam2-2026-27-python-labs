"""Ejercicio 1: Comprobador de triángulos.

Escribe un programa que pida por teclado las longitudes de los tres lados de un
triángulo y compruebe, usando operadores lógicos, si esos tres lados son válidos
para formar un triángulo (la suma de dos lados cualesquiera debe ser siempre
mayor que el tercero). Si son válidos, el programa debe indicar además si el
triángulo es equilátero (los tres lados iguales), isósceles (dos lados iguales)
o escaleno (los tres lados distintos).
"""
import sys

lado = []
for i in range(1, 4):
    valor = float(input(f"Introduce una medida para el lado {i}: "))
    lado.append(valor)

# 1. Validación de lados positivos y desigualdad triangular
if min(lado) <= 0 or (lado[0] >= lado[1] + lado[2] or
                      lado[1] >= lado[0] + lado[2] or
                      lado[2] >= lado[0] + lado[1]):
    print("No es posible construir un triángulo con esas medidas.")
    sys.exit()

# 2. Clasificación
if len(set(lado)) == 1:
    print("El triángulo es válido y es equilátero.")
elif len(set(lado)) == 2:
    print("El triángulo es válido y es isósceles.")
else:
    print("El triángulo es válido y es escaleno.")
