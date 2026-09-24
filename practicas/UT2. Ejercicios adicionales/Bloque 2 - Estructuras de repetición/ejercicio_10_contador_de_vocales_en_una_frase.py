"""Ejercicio 10: Contador de vocales en una frase.

Escribe un programa que pida por teclado una frase y cuente, recorriéndola letra
a letra con un bucle for, cuántas vocales contiene.
"""
count = 0
string = input("Introduce una palabra: ")
for i in string:
    count += 1
print(f"La palabra \"{string}\" contiene {count} letras")