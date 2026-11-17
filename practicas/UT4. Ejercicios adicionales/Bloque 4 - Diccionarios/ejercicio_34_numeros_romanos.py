"""Ejercicio 34: Números romanos.

Nivel: Medio.

Enunciado: Define el diccionario ROMANOS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
"D": 500, "M": 1000}. Escribe:

- es_romano_valido(texto), que devuelva True si el texto (en mayúsculas o minúsculas) no
  está vacío y todas sus letras son símbolos del diccionario;

- y romano_a_entero(texto), que convierta un número romano en entero aplicando la regla
  de la resta: un símbolo cuyo valor es menor que el del símbolo siguiente se resta (en
  XIV, la I se resta de la V), y en caso contrario se suma. Recorre la cadena con
  enumerate() para poder consultar el símbolo siguiente.

Prueba las funciones con "MCMXCIV" (1994), "XLII" (42), "iv" (4), "ABC" y la cadena
vacía.
"""
