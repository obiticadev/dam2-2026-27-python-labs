"""Ejercicio 6: Suma de los primeros números pares.

Escribe un programa que pida por teclado una cantidad N y calcule, usando un
bucle for con range(), la suma de los N primeros números pares (2, 4, 6...).
"""
cantidad = int(input("¿Cuántos números pares quieres sumar? "))
suma = 0

for numero in range(2, 2 * cantidad + 1, 2):
    suma += numero

print(f"La suma de los {cantidad} primeros números pares es: {suma}")
