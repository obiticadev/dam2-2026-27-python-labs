"""Ejercicio 11: Cálculo del factorial de un número.

Escribe un programa que pida por teclado un número entero y calcule su factorial
(el producto de todos los enteros positivos desde 1 hasta ese número) usando un
bucle while.
"""

num = int(input("Introduce un número: "))
calc = 1
for i in range(1, num + 1, 1):
    calc *= i
    
print(f"El resultado es {calc}")