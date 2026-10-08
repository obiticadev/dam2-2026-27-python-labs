"""Ejercicio 10: Ámbito de las variables locales y globales.

Codifica una función mostrar_ambito_variables(), sin parámetros, que cree una
variable local con el mismo nombre que una variable global ya existente y
demuestre por pantalla que ambas son independientes y que la función no
modifica la variable global.
"""
# Variable en el ámbito global
salida = 15


def mostrar_ambito_variables():
    # Variable en el ámbito local (ensombrece a la global dentro de este bloque)
    salida = 10
    print(f"Dentro de la función (ámbito local): salida = {salida}")


print(f"Antes de la llamada (ámbito global): salida = {salida}")

mostrar_ambito_variables()

print(f"Después de la llamada (ámbito global): salida = {salida}")
