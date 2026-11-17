"""Ejercicio 3: Corrector de erratas.

Nivel: Básico.

Enunciado: Como las cadenas son inmutables, corregir una errata obliga a construir una
cadena nueva a partir de trozos de la original. Escribe tres funciones que devuelvan el
texto corregido, usando únicamente slicing y concatenación:

- cambiar_caracter(texto, posicion, nuevo), que sustituya el carácter de esa posición
  por otro;

- quitar_caracter(texto, posicion), que elimine el carácter de esa posición;

- e intercambiar_letras(texto, posicion), que intercambie el carácter de esa posición
  con el siguiente. Si la posición no es válida, la función debe devolver el texto sin
  cambios.

Corrige con ellas las erratas "Hela" → "Hola", "Holla" → "Hola" y "pyhton" → "python", y
comprueba que las variables originales conservan su valor.
"""
