"""Programa principal del ejercicio 13.

Importa el módulo completo con import conversiones y llama a sus funciones
anteponiendo el nombre del módulo: conversiones.nombre_funcion(...).
"""
import conversiones

NUMS = 1
list = []
for i in range(NUMS):
    while True:
        try:
            num = float(input(f"Introduce el número {(i+1):02d}: "))
            if num <= 0:
                raise ValueError("Solo valores positivos\n")
            list.append(round(num, 2))
            break
        except ValueError as e:
            print(e)
valor = list[0]
print(f"{valor} metros a pies son {conversiones.metros_a_pies(valor):,.2f} pies")
print(f"{valor} pies a metros son {conversiones.pies_a_metros(valor):,.2f} metros")
print(
    f"{valor} kilómetros a millas son {conversiones.kilometros_a_millas(valor):,.2f} millas")
