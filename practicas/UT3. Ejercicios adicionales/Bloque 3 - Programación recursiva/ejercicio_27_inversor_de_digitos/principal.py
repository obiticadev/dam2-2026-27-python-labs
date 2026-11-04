"""Ejercicio 27: Inversor recursivo de los dígitos de un número.

Codifica una función recursiva
invertir_numero_recursivo(numero, invertido=0) que invierta el orden de los
dígitos de un número entero positivo, usando un parámetro acumulador con valor
por defecto.
"""


def invertir_numero_recursivo(numero, invertido=0):
    if numero == 0:
        return invertido
    return invertir_numero_recursivo(numero // 10, invertido * 10 + numero % 10)


print(invertir_numero_recursivo(756))
