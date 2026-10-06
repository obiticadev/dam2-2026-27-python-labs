"""Ejercicio 20: Análisis de una serie de temperaturas.

Escribe un programa que, mediante un bucle while, pida temperaturas por teclado
una a una hasta que el usuario escriba "fin". Usa continue para saltar las
lecturas erróneas (marcadas con el valor centinela -999) y break para detener el
análisis en cuanto aparezca una temperatura que supere un umbral de alarma
definido como constante.
"""
import sys
UMBRAL = -999
UMBRAL_ALARMA = 50
while True:
    entrada = input("Introduce una temperatura: ").strip().lower()
    if len(entrada) == 0:
        print("Debes introducri un valor")
    elif entrada == "fin":
        break
    else:
        try:
            temperatura = float(entrada)
            if temperatura > UMBRAL_ALARMA:
                print("Alcanzado el umbral de alarma")
                break
        except ValueError:
            print("ERROR: Asignando -999")
            temperatura = UMBRAL
            continue
