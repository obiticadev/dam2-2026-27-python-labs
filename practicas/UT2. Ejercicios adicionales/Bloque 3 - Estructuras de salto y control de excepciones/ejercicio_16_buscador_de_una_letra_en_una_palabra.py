"""Ejercicio 16: Buscador de una letra en una palabra.

Escribe un programa que recorra, con un bucle for, los caracteres de una palabra
ya creada y busque una letra introducida por teclado, deteniéndose con break en
cuanto la encuentra. Usa la cláusula else del bucle para mostrar un mensaje
distinto si se ha recorrido toda la palabra sin encontrarla.
"""
import sys

while True:
    while True:
        word = input("Introduce una palabra: ")
        char = input("Introduce un carácter: ")

        if len(word) < 1 or len(char) != 1:
            print("Vuelve a intentarlo\n", file=sys.stderr)
        else:
            break
    for i in word:
        if char == i:
            print("Encontrado!\n")
            break
    else:
        print("No se ha encontrado coincidencia\n")
