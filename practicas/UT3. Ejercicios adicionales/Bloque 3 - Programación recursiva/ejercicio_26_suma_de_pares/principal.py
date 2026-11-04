"""Ejercicio 26: Suma recursiva de los números pares hasta n.

Codifica una función recursiva suma_pares_recursivo(n) que calcule la suma de
todos los números pares comprendidos entre 0 y n, ambos incluidos.
"""


def suma_pares_recursivo(n):
    if (n == 0):
        return n
    if (n % 2 == 0):
        return suma_pares_recursivo(n-2) + n
    else:
        n = n-1
        return suma_pares_recursivo(n-2) + n


print(suma_pares_recursivo(9))
