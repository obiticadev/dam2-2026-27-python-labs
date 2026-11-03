"""Ejercicio 21: Suma recursiva de los primeros números naturales.

Codifica una función recursiva suma_recursiva(n) que calcule la suma de los n
primeros números naturales (1 + 2 + ... + n), identificando claramente con
comentarios el caso base y el caso recursivo.
"""


def suma_recursiva(n):
    # Caso base: la suma hasta 0 es 0.
    if n == 0:
        return 0

    # Caso recursivo: n más la suma de los anteriores.
    return n + suma_recursiva(n - 1)


print(suma_recursiva(5))  # 15
