"""Ejercicio 18: Menú con salida inmediata del programa.

Escribe un programa que muestre un menú de opciones dentro de un bucle while
True y que, cuando el usuario elija la opción de salir, termine el programa por
completo con sys.exit() (a diferencia de break, que solo termina el bucle).
"""
import sys


def menu():
    return """
---MENU---
1) Suma
2) Resta

0) Salir
"""


while True:
    print(menu())
    while True:
        try:
            respuesta = int(input("Selecciona una opción: "))
            break
        except ValueError:
            print("Inténtalo de nuevo\n")
    match respuesta:
        case 1:
            print("Has seleccionado Suma")
        case 2:
            print("Has seleccionado Resta")
        case 0:
            print("Has seleccionado Salir")
            sys.exit()
