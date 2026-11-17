"""Ejercicio 38: Plantilla de empleados.

Nivel: Alto.

Enunciado: Los datos de una empresa se guardan como lista de diccionarios con las claves
"nombre", "departamento" y "salario": ("Ana", "Desarrollo", 2400), ("Luis",
"Desarrollo", 2100), ("Marta", "Diseño", 1900), ("Pedro", "Soporte", 1700), ("Elena",
"Diseño", 2000), ("Jorge", "Soporte", 1800) y ("Sara", "Desarrollo", 2600) (construye la
lista a partir de estas siete tuplas). Escribe:

- salario_medio_por_departamento(empleados), que devuelva un diccionario departamento →
  salario medio (redondeado a dos decimales);

- mejor_pagado(empleados, departamento), que devuelva el diccionario del empleado con
  mayor salario de ese departamento (o None si no existe);

- subir_salarios(empleados, departamento, porcentaje), que modifique los diccionarios de
  ese departamento y devuelva cuántos empleados han cambiado;

- y listado_ordenado(empleados), que devuelva una lista nueva ordenada por departamento
  y, dentro de cada departamento, de mayor a menor salario (la función clave_orden debe
  devolver una tupla con el departamento y el salario cambiado de signo).

Muestra los resultados, sube un 10 % los salarios de Soporte y vuelve a mostrar las
medias.
"""
