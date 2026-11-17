"""Ejercicio 40: Índice invertido de frases.

Nivel: Alto.

Enunciado: Un buscador guarda un índice invertido: un diccionario que asocia cada
palabra con la lista de posiciones de las frases en las que aparece. Escribe:

- crear_indice(frases), que reciba una lista de frases y devuelva ese diccionario (las
  palabras en minúsculas y sin signos de puntuación, y cada posición una sola vez por
  palabra);

- buscar(indice, palabra), que devuelva la lista de frases donde aparece la palabra (o
  una lista vacía);

- y buscar_todas(indice, palabras), que devuelva las posiciones de las frases que
  contienen todas las palabras de la lista.

Prueba el índice con ["Python es un lenguaje de programación", "Aprender Python es
divertido", "La programación requiere práctica", "Un lenguaje se aprende con práctica"],
muestra la entrada de algunas palabras y realiza varias búsquedas ("python", "práctica",
["un", "lenguaje"], ["python", "programación"] y una palabra inexistente).
"""
