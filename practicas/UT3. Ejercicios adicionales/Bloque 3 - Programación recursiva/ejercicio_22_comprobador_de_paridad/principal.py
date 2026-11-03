"""Ejercicio 22: Comprobador recursivo de paridad.

Codifica una función recursiva es_par_recursivo(numero) que determine si un
número entero no negativo es par, reduciéndolo de 2 en 2 en cada llamada hasta
llegar a un caso base.
"""


def es_par_recursivo(numero):
    if numero == 0:
        return True
    elif numero == 1:
        return False
    else:
        return es_par_recursivo(numero - 2)


print(es_par_recursivo(28))
