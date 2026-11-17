"""Ejercicio 27: Catálogo de productos (lista de tuplas).

Nivel: Medio.

Enunciado: Un catálogo se guarda como lista de tuplas (nombre, precio): catalogo =
[("teclado", 25.5), ("ratón", 12.0), ("monitor", 189.9), ("auriculares", 35.0),
("cable", 4.5)]. Escribe

- precio_de(catalogo, nombre), que devuelva el precio de un producto o None si no
  existe;

- clave_precio(producto), que devuelva el precio de una tupla del catálogo;

- ordenar_por_precio(catalogo, descendente=False), que devuelva una lista nueva ordenada
  por precio (usa sorted() con key=clave_precio);

- producto_mas_barato(catalogo), que devuelva la tupla del producto más barato (usa
  min() con key);

- y nombres_hasta(catalogo, limite), que devuelva con una lista por comprensión los
  nombres de los productos cuyo precio no supere el límite.

Muestra los resultados y el catálogo ordenado alfabéticamente con un simple
sorted(catalogo).
"""
