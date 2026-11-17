"""Ejercicio 42: De texto CSV a registros.

Nivel: Medio.

Enunciado: Unos datos de personas llegan como lista de líneas de texto con el formato
"nombre;edad;ciudad":

    lineas = [
        "Ana;34;Sevilla",
        "Luis;17;Madrid",
        "Marta;28;Sevilla",
        "Pedro;45;Bilbao",
        "Elena;16;Madrid",
        "Jorge;31;Bilbao",
    ]

Escribe:

- convertir_a_registros(lineas), que devuelva una lista de diccionarios con las claves
  "nombre", "edad" (como int) y "ciudad";

- mayores_de_edad(registros), que devuelva con una comprensión los registros con 18 años
  o más;

- y agrupar_por_ciudad(registros), que devuelva un diccionario que asocie cada ciudad
  con la lista de nombres de las personas que viven en ella.

Muestra el número de mayores de edad y el contenido del diccionario agrupado, ordenando
las ciudades alfabéticamente.

Organización de la plantilla:
- registros.py: desarrolla aquí las funciones del enunciado.
- principal.py: prepara aquí los datos, las pruebas y el programa principal.
"""
