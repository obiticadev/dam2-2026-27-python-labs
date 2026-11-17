"""Ejercicio 50: Intérprete de comandos de una lista de la compra.

Nivel: Alto.

Enunciado: Programa un pequeño intérprete que ejecuta comandos de texto sobre una lista
de la compra guardada en un diccionario producto → cantidad.

Los comandos son:

- añadir producto [cantidad] (si no se indica cantidad se añade 1 unidad y, si el
  producto ya existe, se suman las cantidades),

- quitar producto (elimina el producto),

- ver (muestra la lista ordenada alfabéticamente, un producto por línea con el formato
  producto x cantidad)

- y vaciar.

Escribe:

- ejecutar(comando, compra), que reciba el comando como texto (con mayúsculas y espacios
  irregulares), lo ejecute y devuelva una tupla (ok, mensaje); debe devolver (False,
  ...) con un mensaje explicativo si el comando está vacío, es desconocido, falta el
  producto o se intenta quitar un producto que no está en la lista.

- ejecutar_script(comandos), que cree una compra vacía, ejecute todos los comandos de
  una lista mostrando el mensaje de cada uno, y devuelva una tupla (correctos, erroneos)
  con el recuento.

Pruébalo con una lista de comandos que incluya, al menos, dos comandos erróneos.

Organización de la plantilla:
- interprete_compra.py: desarrolla aquí las funciones del enunciado.
- principal.py: prepara aquí los datos, las pruebas y el programa principal.
"""
