"""Ejercicio 25: Bucle de reintento hasta introducir un número válido.

Escribe un programa que combine un bucle while con try/except: debe repetir la
petición de un número entero positivo por teclado hasta que el usuario introduzca
un valor correcto, terminando el bucle con break. Controla tanto los textos no
numéricos (capturando el ValueError que genera int()) como los números negativos,
lanzando en ese caso un ValueError propio con raise.
"""

while True:
    try:
        num = int(input("Introduce un número positivo: "))
        if num <= 0:
            raise ValueError("Debes introducir un número mayor de 0")
        else:
            print("Número positivo detectado")
            break
    except ValueError as e:
        print(f"ERROR: {e}")
