"""Ejercicio 2: Calculadora de precio con IVA.

Codifica una función calcular_precio_con_iva(precio, iva=21), con un
parámetro por defecto, que calcule el precio final de un producto aplicando el
porcentaje de IVA indicado (21 % si no se especifica otro).
"""


def calcular_precio_con_iva(precio: float, iva: float):
    return (precio * (100 + iva))/100


while True:
    while True:
        try:
            valor = float(input("Introduce un valor: "))
            iva = float(input("Introduce el iva: "))
            break
        except ValueError as e:
            print(e)
    print(
        f"El añadido del {iva}% de IVA sobre {valor}€, es igual a {calcular_precio_con_iva(valor, iva)}€ ")
