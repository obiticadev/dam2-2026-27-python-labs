"""Ejercicio 45: Juego del ahorcado.

Nivel: Medio.

Enunciado: Programa una partida del ahorcado simulada (sin pedir datos por teclado).
Define la constante MAX_FALLOS = 6 y escribe:

- mostrar_palabra(secreta, acertadas), que devuelva la palabra con las letras acertadas
  visibles y las demás sustituidas por _, separadas por espacios ("p _ t _ o _");

- jugar_letra(secreta, letra, acertadas, falladas), que reciba las dos listas de letras
  y las modifique (por referencia) según la letra se encuentre o no en la palabra, y
  devuelva "acierto", "fallo" o "repetida";

- y ha_ganado(secreta, acertadas), que devuelva True si todas las letras de la palabra
  han sido acertadas.

En el programa principal, con la palabra secreta "python" y la lista de intentos ["a",
"p", "e", "y", "p", "t", "i", "h", "o", "n"], juega las letras en orden mientras no se
haya ganado ni se hayan superado los fallos permitidos, mostrando en cada turno el
resultado y el estado de la palabra.

Organización de la plantilla:
- ahorcado.py: desarrolla aquí las funciones del enunciado.
- principal.py: prepara aquí los datos, las pruebas y el programa principal.
"""
