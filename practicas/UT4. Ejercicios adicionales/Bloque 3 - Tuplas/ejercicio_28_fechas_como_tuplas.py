"""Ejercicio 28: Fechas como tuplas.

Nivel: Alto.

Enunciado: Una fecha se representa con una tupla (año, mes, día). Escribe:

- es_anterior(fecha1, fecha2), que devuelva True si la primera fecha es anterior a la
  segunda (aprovecha que Python compara las tuplas elemento a elemento);

- clave_fecha(fecha), que devuelva la tupla reordenada como (mes, día);

- ordenar_fechas(lista_fechas), que devuelva una lista nueva ordenada cronológicamente;

- y fecha_a_texto(fecha), que devuelva un texto con formato "09/03/2026" (los números
  del día y del mes se rellenan con ceros con .zfill(2)).

En el programa principal, prueba las funciones con (2026, 3, 9) y (2025, 12, 31), y
ordena una lista de cinco fechas desordenadas. Después, ordena esa misma lista por (mes,
día) usando sorted() con key=clave_fecha para saber en qué orden caen los cumpleaños
dentro del año.
"""
