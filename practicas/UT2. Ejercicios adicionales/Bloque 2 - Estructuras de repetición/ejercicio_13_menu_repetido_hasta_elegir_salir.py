"""Ejercicio 13: Menú repetido hasta elegir salir.

Escribe un programa que muestre un menú con varias opciones y lo repita
indefinidamente mediante un bucle while, terminando únicamente (con break)
cuando el usuario elige la opción de salir. Las opciones no válidas deben
mostrar un aviso y volver a mostrar el menú.
"""


def mostrar_menu():
    print("""
---MENÚ---
1) Sumar
2) Restar

S) Salir
""")


def sumar():
    # 1. Pedir y validar la cantidad de números
    while True:
        try:
            array_num = int(input("Introduce el número de números a sumar: "))
            if array_num <= 0:
                raise ValueError
            break
        except ValueError:
            print("Introduce un número entero válido mayor que 0.\n")

    # 2. Pedir cada número
    array = []
    for _ in range(array_num):
        while True:
            try:
                num = int(input("Introduce un número: "))
                array.append(num)
                break
            except ValueError:
                print("Introduce un número válido.\n")

    return sum(array)


def resta():
    while True:
        try:
            a = int(input("Introduce el primer número: "))
            b = int(input("Introduce el segundo número: "))
            return a - b
        except ValueError:
            print("Introduce un número válido\n")


while True:
    mostrar_menu()
    respuesta = input("Selecciona una opción: ")
    match respuesta:
        case "1":
            resultado = sumar()
            print(f"El resultado de la suma es: {resultado}")
        case "2":
            resultado = resta()
            print(f"El resultado de la resta es: {resultado}")
        case "s" | "S":
            print("SALIENDO DLE PROGRAMA")
            break
        case _:
            print("Selecciona una opción válida\n")
