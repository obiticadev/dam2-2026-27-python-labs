"""Ejercicio 9: Compresión de texto (RLE).

Nivel: Alto.

Enunciado: La compresión RLE sustituye cada grupo de caracteres iguales consecutivos por
el carácter seguido del número de repeticiones: "aaabbbbcd" se convierte en "a3b4c1d1".

Escribe comprimir(texto), que devuelva el texto comprimido (y la cadena vacía si el
texto está vacío), y descomprimir(comprimido), que haga la operación inversa. Ten en
cuenta que el número de repeticiones puede tener varios dígitos ("w12b1w3"), por lo que
al descomprimir debes ir acumulando los dígitos hasta encontrar la siguiente letra.

Comprueba que descomprimir(comprimir(texto)) devuelve el texto original con "aaabbbbcd",
"wwwwwwwwwwwwbwww" y "abc", y muestra la longitud antes y después de comprimir para ver
en qué casos compensa la compresión.
"""
