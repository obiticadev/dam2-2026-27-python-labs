"""Ejercicio 20: Fusión de listas ordenadas.

Nivel: Alto.

Enunciado: Escribe una función fusionar_ordenadas(a, b) que reciba dos listas de números
ya ordenadas de menor a mayor y devuelva una lista nueva, también ordenada, con todos
sus elementos. No puedes usar sorted() ni .sort(): recorre las dos listas a la vez con
dos índices dentro de un bucle while, añadiendo en cada paso el menor de los dos
elementos que se comparan, y al terminar añade lo que quede de la lista que no se haya
agotado (con slicing). Pruébala con [1, 4, 9] y [2, 3, 10, 11], con una lista vacía, con
elementos repetidos ([1, 2, 2] y [2, 3]) y comprueba en cada caso que el resultado
coincide con sorted(a + b).
"""
