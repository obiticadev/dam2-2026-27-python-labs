"""Ejercicio 24: Contador recursivo de dígitos.

Codifica una función recursiva cuenta_digitos_recursivo(numero) que cuente
cuántos dígitos tiene un número entero positivo.
"""


def cuenta_digitos_recursivo(numero):
    # Caso base: un entero positivo menor que 10 tiene un dígito.
    if numero < 10:
        return 1
    # Caso recursivo: contar la cifra eliminada y las restantes.
    return 1 + cuenta_digitos_recursivo(numero // 10)


print(cuenta_digitos_recursivo(153))
