"""Ejercicio 44: Agrupar anagramas.

Nivel: Medio.

Enunciado: Dos palabras son anagramas si tienen las mismas letras en distinto orden
("roma" y "amor"). Escribe:

- firma(palabra), que devuelva las letras de la palabra ordenadas y unidas en una cadena
  ("roma" → "amor"; usa sorted() y "".join()),

- y agrupar_anagramas(palabras), que devuelva un diccionario cuya clave sea la firma y
  cuyo valor sea la lista de palabras con esa firma.

Por último, construye con una comprensión la lista de grupos que contengan más de una
palabra y muéstralos. Prueba con ["roma", "amor", "mora", "casa", "saca", "perro",
"ramo", "lago", "gola"].

Organización de la plantilla:
- anagramas.py: desarrolla aquí las funciones del enunciado.
- principal.py: prepara aquí los datos, las pruebas y el programa principal.
"""
