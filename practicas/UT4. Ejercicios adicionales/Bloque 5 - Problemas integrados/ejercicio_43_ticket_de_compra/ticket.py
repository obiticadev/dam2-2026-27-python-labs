"""Ejercicio 43: Ticket de compra.

Nivel: Medio.

Enunciado: Una compra se guarda como lista de tuplas (producto, cantidad,
precio_unitario): compra = [("pan", 2, 1.2), ("leche", 3, 0.9), ("queso", 1, 6.5),
("aceite", 2, 8.0)]. Un diccionario guarda el descuento (en %) de algunos productos:
descuentos = {"leche": 10, "aceite": 25}. Escribe:

- importe_linea(cantidad, precio, descuento), que devuelva el importe de una línea con
  el descuento aplicado (redondeado a dos decimales),

- y imprimir_ticket(compra, descuentos), que muestre una línea por producto —con el
  nombre alineado a la izquierda en 10 caracteres (.ljust(10)) y el importe alineado a
  la derecha en 8 (.rjust(8))— y al final el total. Obtén el descuento de cada producto
  con descuentos.get(producto, 0). No te preocupes si algún importe se muestra con un
  solo decimal (por ejemplo, 2.4): el formato con decimales fijos se estudia en la
  siguiente unidad.

Organización de la plantilla:
- ticket.py: desarrolla aquí las funciones del enunciado.
- principal.py: prepara aquí los datos, las pruebas y el programa principal.
"""
