"""Ejercicio 31: Inventario de una tienda.

Nivel: Básico.

Enunciado: El inventario de una tienda se guarda en un diccionario que asocia cada
producto con las unidades disponibles: inventario = {"manzanas": 40, "peras": 25,
"naranjas": 0}. Escribe las funciones:

- reponer(inventario, producto, unidades), que sume unidades a un producto (si el
  producto no existe, lo crea);

- vender(inventario, producto, unidades), que reste unidades y devuelva True si la venta
  es posible o False si el producto no existe o no hay suficientes unidades;

- productos_agotados(inventario), que devuelva la lista de productos con 0 unidades;

- y total_unidades(inventario), que devuelva la suma de todas las unidades (usa
  .values()).

Prueba las cuatro funciones, muestra el inventario con .items() y elimina con del los
productos agotados.
"""
