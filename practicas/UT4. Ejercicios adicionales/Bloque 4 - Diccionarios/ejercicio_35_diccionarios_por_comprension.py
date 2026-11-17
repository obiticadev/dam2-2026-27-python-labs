"""Ejercicio 35: Diccionarios por comprensión.

Nivel: Medio.

Enunciado: Parte del diccionario de precios precios = {"pan": 1.2, "leche": 0.9,
"queso": 6.5, "aceite": 8.0, "sal": 0.5}. Utilizando diccionarios por comprensión,
escribe:

- aplicar_iva(precios, porcentaje), que devuelva un diccionario nuevo con todos los
  precios incrementados (redondeados a dos decimales con round());

- filtrar_caros(precios, limite), que devuelva solo los productos cuyo precio supere el
  límite;

- e invertir(diccionario), que intercambie claves y valores (con {"a": 1, "b": 2}
  devolvería {1: "a", 2: "b"}).

Después, crea un diccionario de ofertas {"pan": 1.0, "sal": 0.4} y utiliza .update()
sobre una copia de precios (precios.copy()) para obtener los precios con las ofertas
aplicadas, sin alterar el diccionario original. Muestra todos los resultados.
"""
