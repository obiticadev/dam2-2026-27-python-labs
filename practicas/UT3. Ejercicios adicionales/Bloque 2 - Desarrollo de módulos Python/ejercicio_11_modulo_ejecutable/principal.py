"""Programa principal del ejercicio 11.

Importa saludar y despedir desde modulo_saludo y utiliza ambas funciones.
Comprueba después la diferencia entre ejecutar este archivo y ejecutar
modulo_saludo.py directamente.
"""
from modulo_saludo import saludar, despedir


nombre = input("¿Cómo te llamas?\n")
print(saludar(nombre))
print(despedir(nombre))
