"""Ejercicio 49: Sopa de letras.

Nivel: Alto.

Enunciado: Una sopa de letras se guarda como una lista de cadenas, todas de la misma
longitud (una por fila):

    sopa = [
        "PYTHONM",
        "ZQUZXDM",
        "MQPZRAE",
        "DXLISTA",
        "QMAVROX",
        "DCMFDSC",
        "QXWVBRK",
    ]

Escribe:

- buscar_en_lineas(lineas, palabra), que devuelva una lista de tuplas (indice_de_linea,
  posicion) con todas las apariciones de la palabra en cada línea (utiliza
  .find(palabra, inicio) dentro de un bucle while para no perderte las apariciones
  repetidas);

- columnas(sopa), que devuelva la lista de columnas como cadenas (construye cada una con
  un bucle y "".join());

- y buscar_palabra(sopa, palabra), que devuelva una lista de tuplas (fila, columna,
  orientacion) con la posición inicial de cada aparición de la palabra, leída de
  izquierda a derecha ("horizontal") o de arriba abajo ("vertical").

Busca PYTHON, LISTA, TUPLA, DATOS y JAVA y muestra el resultado de cada búsqueda con un
mensaje claro cuando la palabra no aparezca.

Organización de la plantilla:
- sopa_letras.py: desarrolla aquí las funciones del enunciado.
- principal.py: prepara aquí los datos, las pruebas y el programa principal.
"""
