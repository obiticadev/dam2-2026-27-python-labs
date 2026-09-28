"""Ejercicio 14: Pirámide de asteriscos.

Escribe un programa que pida por teclado la altura de una pirámide (número de
filas) y la dibuje con asteriscos, usando un bucle for anidado dentro de otro
bucle for: el bucle exterior recorre cada fila y el bucle interior añade tantos
asteriscos como indica el número de fila.
"""
while True:
    try:
        num = int(input("Introduce la altura de la pirámida: "))
        if num <= 0:
            raise ValueError("Introduce un número mayor que 0\n")
        break
    except ValueError as e:
        print(f"ERROR: {e}\nVuelve a intentarlo\n")
for i in range(1, num + 1, 1):
    for j in range(i):
        print("*", end="")
    print()
