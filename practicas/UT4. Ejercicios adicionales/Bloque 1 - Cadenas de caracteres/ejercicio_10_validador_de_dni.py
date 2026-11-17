"""Ejercicio 10: Validador de DNI.

Nivel: Alto.

Enunciado: La letra de un DNI se calcula dividiendo el número entre 23 y usando el resto
como posición en la cadena "TRWAGMYFPDXBNJZSQVHLCKE".

Escribe letra_dni(numero), que devuelva la letra correspondiente a un número de DNI; y
es_dni_valido(dni), que devuelva True si el texto cumple todas estas condiciones:

- tiene 9 caracteres,

- los 8 primeros son dígitos,

- el último es una letra y esa letra coincide con la que corresponde al número.

Antes de validar, la función debe normalizar el texto: quitar espacios sobrantes y
guiones ("12345678-z") y pasarlo a mayúsculas. Pruébala con "12345678Z", "12345678A",
"1234567Z", " 12345678-z " y "ABCDEFGHZ".
"""
