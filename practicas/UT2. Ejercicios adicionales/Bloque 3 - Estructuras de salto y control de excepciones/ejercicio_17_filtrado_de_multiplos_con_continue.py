"""Ejercicio 17: Filtrado de múltiplos con continue.

Escribe un programa que recorra, con un bucle for, los números del 1 al 50 y
muestre únicamente los que son múltiplos de un divisor introducido por teclado,
usando continue para saltar los que no lo son.
"""
while True:
    while True:
        try:
            divisor = int(input("Introduce un divisor: "))
            if divisor <= 0:
                raise ValueError
            break
        except ValueError:
            print("Introduce un número válido")
    for i in range(1, 51):
        if i % divisor != 0:
            continue
        print(i)
