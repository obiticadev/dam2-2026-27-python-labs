"""Ejercicio 5: Clasificador de cuadrante de un punto.

Escribe un programa que pida por teclado las coordenadas x e y de un punto y
determine en qué cuadrante del plano cartesiano se encuentra (primero, segundo,
tercero o cuarto), o si está sobre alguno de los ejes o en el origen de
coordenadas.
"""
while True:
    while True:
        try:
            x = float(input("Coordenada X: "))
            y = float(input("Coordenada Y: "))
            break
        except ValueError as error:
            print(f"Error en\n{error}")
    match x, y:
        case x, y if x > 0 and y > 0:
            print(
                f"Las coordenadas ({x}, {y}), se encuentra en el primer cuadrante")
        case x, y if x < 0 and y > 0:
            print(
                f"Las coordenadas ({x}, {y}), se encuentra en el segundo cuadrante")
        case x, y if x < 0 and y < 0:
            print(
                f"Las coordenadas ({x}, {y}), se encuentra en el tercer cuadrante")
        case x, y if x > 0 and y < 0:
            print(
                f"Las coordenadas ({x}, {y}), se encuentra en el cuarto cuadrante")
        case x, y if x == 0 and y > 0:
            print(
                f"Las coordenadas ({x}, {y}), se encuentra entre el primer y segundo cuadrante")
        case x, y if x == 0 and y < 0:
            print(
                f"Las coordenadas ({x}, {y}), se encuentra entre el tercer y cuarto cuadrante")
        case x, y if x > 0 and y == 0:
            print(
                f"Las coordenadas ({x}, {y}), se encuentra entre el cuarto y primer cuadrante")
        case x, y if x < 0 and y == 0:
            print(
                f"Las coordenadas ({x}, {y}), se encuentra entre el segundo y tercer cuadrante")
        case x, y if x == 0 and y == 0:
            print(
                f"Las coordenadas ({x}, {y}), se encuentra en el origen")
