"""Ejercicio 8: Tabla de multiplicar en orden inverso.

Escribe un programa que pida por teclado un número y muestre su tabla de
multiplicar recorriendo los multiplicadores del 10 al 1 (en orden descendente),
usando un bucle for con range() y un salto negativo.
"""

num = int(input("Introduce un número: "))
print(f"TABLA DE MULTIPLICAR DE {num}")
print("-----------------------------")
for i in range(10, 0, -1):
    print(f"{num} x {i} = {num*i}")