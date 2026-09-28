"""Ejercicio 12: Suma y promedio de varios números.

Escribe un programa que pida por teclado una cantidad N y, a continuación, N
números uno a uno (usando un bucle for con range()), calculando y mostrando al
final su suma total y su promedio.
"""

while True:
    try:
        array_num = int(input("¿Cuántos números quieres introducir?\n"))
        if array_num <= 0:
            raise ValueError("El número debe ser mayor que 0\n")
        break
    except ValueError as e:
        print(f"Error: '{e}',\nVuelve a intentarlo\n")


mi_lista = []
for element in range(array_num):
    while True:
        try:
            element = int(input("Introduce un número: "))
            break
        except ValueError:
            print("Introduce un valor válido\n")
    mi_lista.append(element)
"""
print("La suma de los siguientes números:")
print(*mi_lista, sep=", ")
print(
    f"Es igual a {sum(mi_lista)} y su promedio es de {sum(mi_lista)/array_num}")
"""
numeros_str = ", ".join(str(n) for n in mi_lista)

print(
    f"La suma de los siguientes números: {numeros_str}\n"
    f"Es igual a {sum(mi_lista)} y su promedio es de {sum(mi_lista) / array_num}"
)
