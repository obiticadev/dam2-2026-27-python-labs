"""Ejercicio 5: Perímetro y área de un rectángulo.

Codifica una función calcular_perimetro_area_rectangulo(base, altura) que
calcule a la vez el perímetro y el área de un rectángulo, devolviendo ambos
valores en una tupla.
"""


def calcular_perimetro_area_rectangulo(base: float, altura: float):
    area = base * altura
    perimetro = 2*base + 2*altura
    tupla = (area, perimetro)
    return tupla


while True:
    try:
        base = float(input("Introduce la base: "))
        altura = float(input("Introduce la altura: "))
        tupla = calcular_perimetro_area_rectangulo(base, altura)
        print(
            f"Para la una base con {base} uds y una altura de {altura} uds tenemos un perímetro de {tupla[1]} uds y un area de {tupla[0]} uds^2")
    except ValueError as e:
        print(f"ERROR: {e}")
