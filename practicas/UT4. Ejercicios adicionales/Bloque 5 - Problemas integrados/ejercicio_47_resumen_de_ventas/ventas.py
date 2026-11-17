"""Ejercicio 47: Resumen de ventas.

Nivel: Medio.

Enunciado: Las ventas de una empresa se guardan como lista de tuplas (vendedor,
producto, importe): ventas = [("Ana", "portátil", 900), ("Luis", "ratón", 20), ("Ana",
"ratón", 25), ("Marta", "portátil", 850), ("Luis", "teclado", 45), ("Marta", "ratón",
18), ("Ana", "teclado", 50), ("Luis", "portátil", 920)]. Escribe:

- total_por_vendedor(ventas), que devuelva un diccionario vendedor → importe total;

- mejor_vendedor(totales), que devuelva el nombre del vendedor con mayor importe;

- ventas_por_producto(ventas), que devuelva un diccionario producto → lista de los
  importes de sus ventas;

- y producto_mas_vendido(por_producto), que devuelva el producto con más ventas (más
  elementos en su lista).

Muestra un informe con los totales ordenados de mayor a menor importe, el mejor
vendedor, el número de ventas de cada producto (ordenados alfabéticamente) y el producto
más vendido.

Organización de la plantilla:
- ventas.py: desarrolla aquí las funciones del enunciado.
- principal.py: prepara aquí los datos, las pruebas y el programa principal.
"""
