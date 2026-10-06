"""Ejercicio 22: Acceso seguro a un carácter de una palabra.

Escribe un programa que, dada una palabra ya creada, pida por teclado una
posición e intente acceder a ese carácter de la palabra, controlando con
try/except un posible IndexError si la posición no existe.
"""

palabra = "hola"
while True:
    while True:
        try:
            posicion = int(
                input("Introduce una posición positiva para devolver el caracter: "))
            if posicion <= 0:
                raise ValueError
            else:
                break
        except ValueError:
            print("ERROR: Introduce un valor numérico")
    try:
        print(palabra[posicion - 1])
    except IndexError:
        print("Fuera de rango")
