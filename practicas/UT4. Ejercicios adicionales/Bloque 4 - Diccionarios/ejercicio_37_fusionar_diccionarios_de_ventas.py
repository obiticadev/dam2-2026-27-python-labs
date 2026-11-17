"""Ejercicio 37: Fusionar diccionarios de ventas.

Nivel: Medio.

Enunciado: Dos tiendas guardan las unidades vendidas de cada producto en sendos
diccionarios: tienda1 = {"pan": 30, "leche": 20, "huevos": 15} y tienda2 = {"leche": 25,
"huevos": 10, "queso": 8}. Escribe:

- fusionar_sumando(d1, d2), que devuelva un diccionario nuevo con los productos de ambas
  tiendas, sumando las unidades de los productos que aparecen en las dos (no debe
  modificar ninguno de los diccionarios originales);

- claves_comunes(d1, d2), que devuelva la lista de productos presentes en ambas tiendas;

- y claves_exclusivas(d1, d2), que devuelva la lista de productos que solo vende d1.

En ambos casos utiliza listas por comprensión. Comprueba al final que los diccionarios
originales no han cambiado.
"""
