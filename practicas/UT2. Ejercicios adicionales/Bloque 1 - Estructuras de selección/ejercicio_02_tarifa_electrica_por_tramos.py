"""Ejercicio 2: Tarifa eléctrica por tramos.

Escribe un programa que pida por teclado el consumo eléctrico mensual, en kWh,
y calcule el importe a pagar aplicando un precio por kWh distinto según el tramo
de consumo: un precio para consumos de hasta 200 kWh, otro precio (más caro) para
consumos entre 200 y 400 kWh, y un tercer precio (el más caro) para consumos
superiores a 400 kWh. Los precios y los límites de cada tramo deben definirse
como constantes.
"""


LIMITE_BAJO = 200
LIMITE_MEDIO = 400

PRECIO_BAJO = 0.5
PRECIO_MEDIO = 0.7
PRECIO_ALTO = 0.9

while True:
    try:
        consumo = float(input("Introduce el consumo eléctrico mensual en kWh: "))
        print(f"Has introducido: {consumo}")
        break
    except ValueError:
        print("Error: No has introducido un número válido")
    

match consumo:
    case c if c < 0:
        print("El consumo no puede ser menor que 0")
    case c if c <= LIMITE_BAJO:
        precio = consumo * PRECIO_BAJO
        print(f"El precio resultante es de {precio}")
    case c if c <= LIMITE_MEDIO:
        precio = consumo * PRECIO_MEDIO
        print(f"El precio resultante es de {precio}")
    case _:
        precio = consumo * PRECIO_ALTO
        print(f"El precio resultante es de {precio}")