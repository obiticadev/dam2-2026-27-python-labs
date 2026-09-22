"""Ejercicio 5: Clasificador de cuadrante de un punto.

Escribe un programa que pida por teclado las coordenadas x e y de un punto y
determine en qué cuadrante del plano cartesiano se encuentra (primero, segundo,
tercero o cuarto), o si está sobre alguno de los ejes o en el origen de
coordenadas.
"""
while True:
    try:
        x = float(input("Coordenada X: "))
        y = float(input("Coordenada Y: "))
        break
    except ValueError as error:
        print(f"Error en\n{error}")



