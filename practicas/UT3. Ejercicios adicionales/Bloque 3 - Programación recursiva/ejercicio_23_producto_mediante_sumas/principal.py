"""Ejercicio 23: Producto recursivo mediante sumas sucesivas.

Codifica una función recursiva producto_recursivo(a, b) que calcule el producto
de dos números mediante sumas sucesivas, sin usar el operador * en el caso
recursivo.
"""


def producto_recursivo(a, b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + (producto_recursivo(a, b-1))


print(producto_recursivo(8, 9))
