"""Ejercicio 3: Comprobador de mayoría de edad.

Codifica una función es_mayor_de_edad(edad) que devuelva True o False según si
la edad recibida corresponde a una persona mayor de edad (18 años o más).
"""

MAYORIA_DE_EDAD = 18


def es_mayor_de_edad(edad: int):
    if edad >= MAYORIA_DE_EDAD:
        return True
    else:
        return False


while True:
    while True:
        try:
            valor = float(input("Introduce una edad: "))
            break
        except ValueError as e:
            print(e)
    print(
        f"Para una persona con {valor} años se consideraría mayor: {es_mayor_de_edad(valor)} ")
