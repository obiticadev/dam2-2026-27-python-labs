"""Ejercicio 25: Conversor recursivo de decimal a binario.

Codifica una función recursiva decimal_a_binario_recursivo(numero) que devuelva,
como cadena de texto, la representación en binario de un número entero no
negativo escrito en decimal.
"""


def decimal_a_binario_recursivo(numero):
    if numero == 0 or numero == 1:
        return str(numero)
    return decimal_a_binario_recursivo(numero // 2) + str(numero % 2)


print(decimal_a_binario_recursivo(7))
