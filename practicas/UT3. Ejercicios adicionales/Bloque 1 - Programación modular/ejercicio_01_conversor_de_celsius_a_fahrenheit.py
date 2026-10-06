"""Ejercicio 1: Conversor de Celsius a Fahrenheit.

Codifica una función celsius_a_fahrenheit(celsius) que convierta una
temperatura de grados Celsius a grados Fahrenheit, aplicando la fórmula:

    F = C * 9 / 5 + 32
"""
try:
    celsius = float(input("Introduce la temperatura en celsius: "))
except ValueError as e:
    print(e)

Fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius}ºC son {Fahrenheit}ºF")
