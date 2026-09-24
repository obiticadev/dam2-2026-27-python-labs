"""Ejercicio 7: Adivina el número secreto.

Escribe un programa que genere un número secreto al azar entre 1 y 100 (con el
módulo random) y repita la petición de un intento al usuario, mediante un bucle
while, hasta que lo acierte. En cada intento fallido, el programa debe indicar si
el número secreto es mayor o menor que el intento introducido, y al final debe
mostrar en cuántos intentos se ha acertado.
"""

import random

num = random.randrange(100)+1
print(num)

while True:
    select = int(input("Introduce un número: "))
    if select > num:
        print("-")
    elif select < num:
        print("+")
    else:
        print("BINGO")
        break