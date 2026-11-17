"""Ejercicio 25: Modificar una tupla sin modificarla.

Nivel: Medio.

Enunciado: Como las tuplas son inmutables, para "cambiarlas" hay que crear otra.
Escribe:

- reemplazar_elemento(tupla, posicion, valor), que devuelva una tupla nueva igual a la
  original pero con el elemento de esa posición sustituido (conviértela a lista con
  list(), modifícala y vuelve a convertirla con tuple());

- y anadir_elemento(tupla, valor), que devuelva una tupla nueva con el valor al final
  (recuerda que una tupla de un solo elemento se escribe (valor,), con coma).

Prueba ambas con colores = ("rojo", "verde", "azul") y comprueba que colores no ha
cambiado. Después, crea registro = ("Ana", [7, 8]), una tupla que contiene una lista,
añade una nota a esa lista con .append() y explica en un comentario por qué Python lo
permite aunque registro sea una tupla.
"""
