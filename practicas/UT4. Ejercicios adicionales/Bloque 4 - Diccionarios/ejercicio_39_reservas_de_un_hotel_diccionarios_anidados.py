"""Ejercicio 39: Reservas de un hotel (diccionarios anidados).

Nivel: Alto.

Enunciado: Las habitaciones de un hotel se guardan en un diccionario cuyas claves son
los números de habitación y cuyos valores son otros diccionarios con el "tipo", el
"precio" por noche y el "cliente" que la ocupa (None si está libre): hotel = {101:
{"tipo": "individual", "precio": 60, "cliente": None}, 102: {"tipo": "doble", "precio":
90, "cliente": None}, 103: {"tipo": "doble", "precio": 95, "cliente": None}, 201:
{"tipo": "suite", "precio": 150, "cliente": None}}. Escribe:

- reservar(hotel, habitacion, cliente), que devuelva (True, mensaje) si la reserva se
  realiza o (False, motivo) si la habitación no existe o ya está ocupada;

- liberar(hotel, habitacion), que deje la habitación libre y devuelva True si estaba
  ocupada;

- habitaciones_libres(hotel, tipo=None), que devuelva la lista ordenada de números de
  habitaciones libres (si se indica tipo, solo las de ese tipo);

- buscar_cliente(hotel, cliente), que devuelva la lista de habitaciones que ocupa;

- e ingresos_por_noche(hotel), que devuelva la suma de los precios de las habitaciones
  ocupadas.

Prueba las cinco funciones con varias reservas, incluidas dos erróneas.
"""
