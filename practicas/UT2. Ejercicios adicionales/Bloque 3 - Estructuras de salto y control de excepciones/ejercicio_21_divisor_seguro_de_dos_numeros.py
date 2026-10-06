"""Ejercicio 21: Divisor seguro de dos números.

Escribe un programa que pida dos números por teclado y calcule su división,
controlando con try/except tanto el caso de que el texto introducido no sea un
número válido (ValueError) como el de una división entre cero
(ZeroDivisionError), mostrando el resultado en la cláusula else solo si no se ha
producido ningún error.
"""
try:
    num1 = int(input("Introduce el número 1: "))
    num2 = int(input("Introduce el número 2: "))
    division = num1 / num2
except ValueError:
    print("Debes introducir números enteros válidos.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
else:
    print(f"La división es igual a {division}")
