"""Ejercicio 26: Horario de clases (tuplas como claves).

Nivel: Medio.

Enunciado: El horario semanal de un grupo se guarda en un diccionario cuyas claves son
tuplas (dia, hora) y cuyos valores son las asignaturas: horario = {("lunes", 1):
"Programación", ("lunes", 2): "Programación", ("martes", 1): "Bases de datos",
("miércoles", 3): "Entornos", ("jueves", 2): "Programación"}. Escribe:

- que_toca(horario, dia, hora), que devuelva la asignatura o "libre" (usa .get());

- asignar(horario, dia, hora, asignatura), que ocupe una hora solo si está libre y
  devuelva True o False;

- horas_de_asignatura(horario, asignatura), que devuelva la lista de tuplas (dia, hora)
  en las que se imparte;

- y clases_del_dia(horario, dia), que devuelva una lista de tuplas (hora, asignatura)
  ordenada por hora (recorre los pares con .items() y desempaqueta cada clave). Prueba
  las cuatro funciones y muestra el horario final.
"""
