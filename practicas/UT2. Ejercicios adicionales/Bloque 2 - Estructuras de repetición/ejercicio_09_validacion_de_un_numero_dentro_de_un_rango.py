"""Ejercicio 9: Validación de un número dentro de un rango.

Escribe un programa que, mediante un bucle while, repita la petición de un
número por teclado mientras el valor introducido esté fuera de un rango
permitido (definido mediante dos constantes, valor mínimo y valor máximo),
mostrando un aviso en cada intento fallido y el número finalmente válido al
terminar.
"""
VALUE_MIN = 10
VALUE_MAX = 20

while True:
    num = int(input("Introduce un número: "))
    if num > VALUE_MIN and num < VALUE_MAX:
        print("BINGO")
        break
    else:
        print("Fallaste")
