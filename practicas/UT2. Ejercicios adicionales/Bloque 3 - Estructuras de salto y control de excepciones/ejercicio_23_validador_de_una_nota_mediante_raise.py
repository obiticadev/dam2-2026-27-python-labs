"""Ejercicio 23: Validador de una nota mediante raise.

Escribe un programa que pida una nota por teclado (0-10) y, si está fuera de ese
rango, lance (raise) un ValueError con un mensaje descriptivo. Captura después
ese error con try/except para mostrar el mensaje al usuario.
"""
while True:
    try:
        num = int(input("Introduce un número del 0 - 10: "))
        if num < 0 or num > 10:
            raise ValueError(f"ERROR: {num} se sale del rango")
    except ValueError as e:
        print(e)
