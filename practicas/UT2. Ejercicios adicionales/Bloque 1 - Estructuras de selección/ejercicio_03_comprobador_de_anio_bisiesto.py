"""Ejercicio 3: Comprobador de año bisiesto.

Escribe un programa que pida por teclado un año y compruebe si es bisiesto,
aplicando la regla del calendario gregoriano: un año es bisiesto si es divisible
entre 4, excepto si es divisible entre 100 (en cuyo caso no lo es), salvo que
además sea divisible entre 400 (en cuyo caso sí lo es). Combina estas condiciones
con operadores lógicos (and, or) en una única expresión booleana.
"""
while True:
    año = float(input("Introduce un año: "))
    if (año % 4 == 0 and año % 100 != 0 or año % 400 == 0):
        print("Es bisiesto")
    else:
        print("No es bisiesto")