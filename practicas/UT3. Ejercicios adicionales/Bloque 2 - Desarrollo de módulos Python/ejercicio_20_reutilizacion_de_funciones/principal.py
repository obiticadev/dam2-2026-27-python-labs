"""Programa principal del ejercicio 20.

Importa únicamente area_cuadrado y perimetro_cuadrado desde geometria2.py y
comprueba que ambas funcionan correctamente.
"""
from geometria2 import area_cuadrado, perimetro_cuadrado

if __name__ == "__main__":
    resultado_area = area_cuadrado(4)
    resultado_perimetro = perimetro_cuadrado(4)

    print(f"Área del cuadrado (lado 4): {resultado_area}")
    print(f"Perímetro del cuadrado (lado 4): {resultado_perimetro}")
