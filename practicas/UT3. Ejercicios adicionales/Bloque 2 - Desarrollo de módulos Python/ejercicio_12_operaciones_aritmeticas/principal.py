"""Programa principal del ejercicio 12.

Importa las cuatro funciones mediante:

    from operaciones import sumar, restar, multiplicar, dividir

Utiliza todas las funciones desde este archivo.
"""
from operaciones import sumar, restar, multiplicar, dividir
NUMS = 3
numeros = []
for i in range(NUMS):
    while True:
        try:
            num = float(input(f"Introduce el número {i+1}: "))
            numeros.append(num)
            break
        except ValueError as e:
            print(e)
print(f"{sumar.__qualname__} = {sumar(numeros[0], numeros[1])}")
print(f"{restar.__qualname__} = {restar(numeros[0], numeros[1])}")
print(f"{multiplicar.__qualname__} = {multiplicar(numeros[0], numeros[1])}")
print(f"{dividir.__qualname__} = {dividir(numeros[0], numeros[1])}")
print(f"{dividir.__qualname__} = {dividir(numeros[0], numeros[2])}")
