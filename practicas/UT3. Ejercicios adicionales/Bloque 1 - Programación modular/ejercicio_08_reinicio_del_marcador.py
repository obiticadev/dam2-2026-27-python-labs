"""Ejercicio 8: Reinicio del marcador de una partida.

Codifica una función reiniciar_marcador(marcador) que reciba un int con el
marcador de una partida e intente ponerlo a cero. Comprueba que, tras la
llamada, la variable original no ha cambiado por tratarse de un tipo inmutable.
"""


def reiniciar_marcador(marcador: int):
    marcador = 0


while True:
    while True:
        try:
            num = int(input("Introduce un número: "))
            if num < 0:
                raise ValueError("Introduce un número entero positivo\n")
            print(f"El marcador antes estaba en {num}")
            break
        except ValueError as e:
            print(e)
    reiniciar_marcador(num)
    print(f"El marcador ahora es de {num}")
