"""Ejercicio 7: Incremento de la puntuación de una partida.

Codifica una función incrementar_puntuacion(lista_puntuaciones, puntos) que
reciba una lista de puntuaciones de una partida y le añada, con .append(), una
nueva puntuación. Comprueba que la lista original queda modificada tras la
llamada.
"""


def incrementar_puntuacion(lista_puntuaciones: list, puntos: int) -> None:
    lista_puntuaciones.append(puntos)


lista = [5, 3, 2]

while True:
    try:
        punto = int(input("Introduce un número entero positivo: "))

        # 'if' estándar: evita el SyntaxError
        if punto <= 0:
            raise ValueError("Solo valores positivos\n")

        incrementar_puntuacion(lista, punto)
        print(f"Lista tras la modificación: {lista}")
        break  # Termina el bucle tras añadir el valor correctamente

    except ValueError as e:
        print(e)
