"""Ejercicio 14: Ranking de puntuaciones.

Nivel: Medio.

Enunciado: Escribe una función obtener_mejores(puntuaciones, cantidad) que devuelva una
lista nueva con las cantidad puntuaciones más altas, de mayor a menor (usa sorted() con
reverse=True y slicing), sin modificar la lista original. En el programa principal,
parte de la lista [640, 910, 785, 430, 995, 870]: muestra el ranking de las tres mejores
con el formato 1º: 995 usando enumerate(); añade una nueva puntuación con .append() y
vuelve a mostrar el ranking; y elimina de la lista original la peor puntuación (obtenida
con min()) usando .remove(), mostrando finalmente la lista resultante y la mejor
puntuación con max().
"""
