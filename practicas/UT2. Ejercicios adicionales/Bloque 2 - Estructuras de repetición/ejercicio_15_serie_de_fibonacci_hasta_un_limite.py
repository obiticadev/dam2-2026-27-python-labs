"""Ejercicio 15: Serie de Fibonacci hasta un límite.

Escribe un programa que pida por teclado un número límite y muestre, mediante un
bucle while, los términos de la serie de Fibonacci (cada término es la suma de
los dos anteriores, empezando por 0 y 1) hasta que se supera ese límite.
"""
while True:
    try:
        limit = int(input("Introduce el límite para Fibonacci: "))
        if limit <= 0:
            raise ValueError("Introduce un número mayor que 0")
        break
    except ValueError as e:
        print(f"ERROR: {e}\nInténtalo de nuevo\n")

a = 0
b = 1
while a <= limit:
    print(a, end=" ")
    a, b = b, a + b

print()  # Salto de línea final
