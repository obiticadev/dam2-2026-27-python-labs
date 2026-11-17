"""Ejercicio 16: Dividir una lista en bloques.

Nivel: Medio.

Enunciado: Escribe una función trocear(lista, tamano) que divida una lista en bloques de
tamano elementos y devuelva una lista de listas; el último bloque puede tener menos
elementos (por ejemplo, [1, 2, 3, 4, 5, 6, 7] en bloques de 3 da [[1, 2, 3], [4, 5, 6],
[7]]). Utiliza range(0, len(lista), tamano) para recorrer las posiciones de inicio de
cada bloque y slicing para extraerlos. Escribe también la función inversa
aplanar(lista_de_listas), que reúna todos los elementos de los bloques en una única
lista mediante dos bucles for anidados. Prueba las funciones con los números del 1 al 10
en bloques de 4 y de 3, con una lista vacía, y comprueba que aplanar(trocear(lista, n))
devuelve la lista original. Por último, reparte en equipos de 2 personas la lista de
nombres ["Ana", "Luis", "Marta", "Pedro", "Elena", "Jorge"].
"""
