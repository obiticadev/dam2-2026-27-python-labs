"""Programa principal del ejercicio 18.

Importa todos los nombres del módulo mediante:

    from modulo_fecha import *

Utiliza desde aquí sus tres funciones.
"""

from modulo_fecha import *

dia = 16
dia2 = 12
mes = 11
anio = 1900
anio_nacimiento = 1992
anio_actual = 2030

print(es_fecha_valida(dia, mes))
print(es_fecha_valida(dia2, mes))
print(es_bisiesto(anio))
print(edad_en_anios(anio_nacimiento, anio_actual))
