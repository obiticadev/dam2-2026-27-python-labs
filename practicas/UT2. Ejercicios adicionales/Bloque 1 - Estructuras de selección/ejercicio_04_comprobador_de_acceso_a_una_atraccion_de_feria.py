"""Ejercicio 4: Comprobador de acceso a una atracción de feria.

Escribe un programa que pida por teclado la edad y la altura (en cm) de una
persona y determine si puede acceder a una atracción de feria que exige una edad
mínima y una altura mínima, definidas como constantes. Si no cumple la edad
mínima pero sí una edad y una altura reducidas (también definidas como
constantes), el acceso debe permitirse igualmente, pero acompañada de una
persona adulta. En cualquier otro caso, el acceso debe denegarse.
"""

EDAD_MINIMA = 18
ALTURA_MINIMA = 1.5

while True:
    while True:
        try:
            edad = float(input("Introduce la edad: "))
            altura = float(input("Introduce la altura: "))
            break
        except ValueError as error:
            print(f"Error en {error}")

    if edad > EDAD_MINIMA and altura > ALTURA_MINIMA:
        print("Acceso permitido")
    elif edad < EDAD_MINIMA and altura > ALTURA_MINIMA:
        print("Acceso permitido, pero acompañado de una persona adulta")
    else:
        print("Acceso denegado")
