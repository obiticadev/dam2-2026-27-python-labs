"""Ejercicio 36: Escrutinio de votos.

Nivel: Medio.

Enunciado: Una votación se guarda como una lista con el nombre del candidato elegido en
cada papeleta. Escribe:

- recuento(votos), que devuelva un diccionario candidato → número de votos (usa .get());

- ganadores(resultado), que devuelva la lista de candidatos con más votos (puede haber
  empate, por lo que no basta con max() sobre las claves);

- y porcentajes(resultado), que devuelva, con un diccionario por comprensión, el
  porcentaje de votos de cada candidato redondeado a un decimal.

Prueba las funciones con ["Ana", "Luis", "Ana", "Marta", "Luis", "Ana", "Luis", "Marta",
"Luis"] y con una votación empatada (["Ana", "Luis", "Ana", "Luis"]).
"""
