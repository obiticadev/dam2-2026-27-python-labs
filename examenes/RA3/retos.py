"""
Oliver Bitica 03-11-2026

Se ocupa de ejecutar las diferentes funciones descritas por el examen del RA3
"""


"""
Suma todos los divisores del número menores que el.

n es el número que se usará para sacar sus divisores y sumarlos.
Devuelve la suma de sus divisores.
"""
def suma_divisores(n):
    suma = 0
    for num in range(n):
        if num == 0:
            continue
        if n % num == 0:
            suma += num
    return suma

"""
Clasifica el total resultante de la llamada a la función suma_divisores()

n es el número que se usará para llamar la función suma_divisores() y clasificar así su resultado
Devuelve el string del resultado de la clasificación; perfecto para cuando coincida la suma de sus divisores con n, abundante cuando la suma sobrepasa n y deficiente cuando la suma no alcanza a n
"""
def tipo_numero(n):
    num = suma_divisores(n)
    if num == n:
        return "perfecto"
    elif num > n:
        return "abundante"
    else:
        return "deficiente"

"""
Itera el valor hasta que llegue a 1 de forma que si es par se divide entre 2 y si es impar se multiplica por 3 y se le suma 1

n es el número que se usará para la secuencia de collatz.
Devuelve el número de pasos que ha realizado hasta que n alcance el valor de 1
"""
def pasos_collatz(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n/2
            count += 1
        else:
            n = n * 3 + 1
            count += 1
    return count

"""
Itera el valor de forma recursiva llamándose a sí misma cuando el valor no es igual a 1 diferenciando dos casos recursivos, A para cuando el valor es par para dividir entre 2 y B para cuando el valor es impar se multiplica por 3 y suma 1

n es el número que se usará para la secuencia de collatz.
Devuelve el número de pasos que ha realizado hasta que n alcance el valor de 1
"""

def pasos_collatz_recursivo(n):
    count = 0
    # Caso base
    if n == 1:
        return count
    # Caso recursivo A
    if n % 2 == 0:
        count += 1
        return count + pasos_collatz_recursivo(n/2)
    # Caso recursivo B
    count += 1
    return count + pasos_collatz_recursivo(n * 3 + 1)
"""
Entrega una fila y columna del triángulo de pascal para pintarla

n es la fila a la que apuntaría de la pirámida
k es la posición de dicha fila que recorre
devuelve el valor en dicha fila
"""
def combinatorio(n, k):
    pass

"""
Pinta la salida en string de la fila indicada

n es la fila de la pirámide de pascal
"""
def mostrar_fila_pascal(n):
    pass

"""
Agrega un texto a una lista

historial es la lista mutable
texto el string que se agregará
"""
def anotar(historial, texto):
    historial.append(texto)

"""
Suma una cantidad a puntos

puntos es el valor que será sumado
cantidad el valor por el que aumentará puntos
Devuelve la suma de puntos y cantidad
"""
def sumar_puntos(puntos, cantidad):
    puntos += cantidad
    return puntos




if __name__ == "__main__":
    while True:
        try:
            num_entero = int(input("Introduce un número entero positivo: "))
            if num_entero <= 0:
                raise ValueError("el número debe ser mayor que 0")
        except ValueError as e:
            print(f"Error: {e}")
            continue


        linea1 = f"{num_entero} es un número {tipo_numero(num_entero)} (suma de divisores: {suma_divisores(num_entero)})"
        print(linea1)

        linea2 = f"Pasos de Collatz -> iterativo: {pasos_collatz(num_entero)} | recursivo: {pasos_collatz_recursivo(num_entero)}"
        print(linea2)
        if (num_entero <= 15):
            print(f"Fila {num_entero} del triángulo de Pascal:")
        puntos = num_entero
        sumar_puntos(puntos, cantidad=5)
        puntos_guardados = sumar_puntos(puntos, cantidad=5)

        print(f"Puntos sin guardar el resultado: {puntos}")
        print(f"Puntos guardando el resultado: {puntos_guardados}")

        historial = [linea1]
        anotar(historial,linea2)
        print(historial)
        