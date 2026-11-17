"""Ejercicio 11: Lista de la compra.

Nivel: Básico.

Enunciado: Escribe un programa para gestionar una lista de la compra con las siguientes
funciones:

- anadir_producto(lista, producto), que añade el producto al final solo si todavía no
  está en la lista y devuelve True si lo ha añadido o False en caso contrario;

- quitar_producto(lista, producto), que lo elimina si está y devuelve True/False igual
  que la anterior;

- y mostrar_lista(lista), que muestra los productos numerados a partir de 1 con
  enumerate().

En el programa principal, parte de una lista con tres productos, prueba las tres
funciones (incluido un producto repetido y un producto inexistente), inserta un producto
urgente al principio con .insert(), elimina el último con .pop() y comprueba que las
funciones modifican la lista original sin devolverla (paso por referencia).
"""
