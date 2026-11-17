"""Ejercicio 46: Agenda de cumpleaños.

Nivel: Medio.

Enunciado: Un diccionario guarda el cumpleaños de varias personas como una tupla (dia,
mes): cumples = {"Ana": (15, 3), "Luis": (6, 10), "Marta": (30, 11), "Pedro": (1, 1),
"Elena": (24, 12), "Jorge": (2, 10)}. Escribe:

- clave_cumple(elemento), que reciba una pareja (nombre, (dia, mes)) y devuelva la tupla
  (mes, dia) para poder ordenar dentro del año;

- proximos_cumpleanos(cumples, dia_actual, mes_actual), que devuelva la lista de parejas
  (nombre, (dia, mes)) empezando por los cumpleaños de hoy o posteriores (en orden) y
  continuando con los que ya han pasado este año (también en orden);

- y cumpleaneros_del_mes(cumples, mes), que devuelva con una comprensión los nombres de
  quienes cumplen años en ese mes.

Prueba las funciones suponiendo que hoy es el 6 de octubre.

Organización de la plantilla:
- cumpleanos.py: desarrolla aquí las funciones del enunciado.
- principal.py: prepara aquí los datos, las pruebas y el programa principal.
"""
