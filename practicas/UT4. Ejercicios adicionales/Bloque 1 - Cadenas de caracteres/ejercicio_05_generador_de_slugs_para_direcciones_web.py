"""Ejercicio 5: Generador de «slugs» para direcciones web.

Nivel: Medio.

Enunciado: Un «slug» es la parte de una dirección web que identifica un artículo: va en
minúsculas, sin tildes y con las palabras unidas por guiones (por ejemplo,
"introduccion-a-python").

Escribe una función crear_slug(titulo) que convierta un título en su slug:

- elimina los espacios sobrantes de los extremos,

- pasa el texto a minúsculas,

- sustituye las vocales con tilde y la ñ por una n (á→a, é→e, í→i, ó→o, ú→u, ñ→n)

- y une las palabras con guiones, aunque haya varios espacios seguidos entre ellas.

Utiliza .strip(), .lower(), .replace(), .split() y .join().
"""
