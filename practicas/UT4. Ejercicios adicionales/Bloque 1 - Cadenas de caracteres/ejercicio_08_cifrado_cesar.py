"""Ejercicio 8: Cifrado César.

Nivel: Alto.

Enunciado: El cifrado César sustituye cada letra por la que está d posiciones más
adelante en el alfabeto (con d = 3, la a pasa a ser d y la x pasa a ser a).

Define la constante ALFABETO = "abcdefghijklmnopqrstuvwxyz" y escribe:

- cifrar_cesar(texto, desplazamiento), que cifre las letras del alfabeto y deje intactos
  los demás caracteres (usa .index() para localizar la letra y el operador % para volver
  al principio del alfabeto);

- descifrar_cesar(texto, desplazamiento), que reutilice la función anterior;

- y romper_cesar(texto_cifrado, palabra_conocida), que pruebe los 26 desplazamientos
  posibles y devuelva el que haga aparecer palabra_conocida en el texto descifrado (o
  None si no lo consigue). El texto de entrada estará en minúsculas.

Comprueba que cifrar y descifrar "nos vemos en la biblioteca" con desplazamiento 7
devuelve el texto original y utiliza romper_cesar para recuperarlo sin conocer el
desplazamiento.
"""
