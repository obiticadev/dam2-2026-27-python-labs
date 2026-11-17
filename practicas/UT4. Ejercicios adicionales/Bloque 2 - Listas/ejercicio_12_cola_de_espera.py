"""Ejercicio 12: Cola de espera.

Nivel: Básico.

Enunciado: La cola de espera de una consulta médica se guarda en una lista de nombres:
el primero de la lista es el siguiente en ser atendido. Escribe las funciones

- llegar(cola, nombre), que añada una persona al final de la cola;

- atender(cola), que elimine y devuelva a la primera persona de la cola (o None si la
  cola está vacía);

- posicion_en_cola(cola, nombre), que devuelva el puesto que ocupa una persona empezando
  a contar en 1 (o 0 si no está en la cola);

- y dar_prioridad(cola, nombre), que mueva a una persona al principio de la cola (con
  .remove() e .insert()).

Parte de la cola ["Ana", "Luis", "Marta"]: llega Pedro, atiende dos personas, consulta
la posición de Marta y de Ana, da prioridad a Pedro y muestra la cola tras cada
operación.
"""
