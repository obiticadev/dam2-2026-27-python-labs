"""Ejercicio 19: Módulo de cálculos financieros.

Crea calcular_interes_simple(capital, tasa, tiempo),
calcular_capital_final_simple(capital, tasa, tiempo), que debe reutilizar la
función anterior, y calcular_descuento(precio, porcentaje). Añade un bloque de
pruebas protegido con if __name__ == "__main__":.
"""


def calcular_interes_simple(capital, tasa, tiempo):
    # El interés simple es el producto de las tres variables
    return capital * tasa * tiempo


def calcular_capital_final_simple(capital, tasa, tiempo):
    # El enunciado pide REUTILIZAR la función anterior (Capital Final = Capital Inicial + Interés)
    interes = calcular_interes_simple(capital, tasa, tiempo)
    return capital + interes


def calcular_descuento(precio, porcentaje):
    # Porcentaje viene como entero (ej: 15 para 15%), lo dividimos por 100
    descuento = precio * (porcentaje / 100)
    return precio - descuento


if __name__ == "__main__":
    print("--- PRUEBAS DEL MÓDULO FINANCIERO ---")

    # 1. Prueba de Interés Simple
    # Ejemplo: $10,000 al 5% (0.05) anual durante 3 años
    i_simple = calcular_interes_simple(10000, 0.05, 3)
    print(f"Interés simple generado: ${i_simple} (Esperado: $1500.0)")

    # 2. Prueba de Capital Final
    # Ejemplo: Mismos datos anteriores, el total debería ser $11,500
    c_final = calcular_capital_final_simple(10000, 0.05, 3)
    print(f"Capital final acumulado: ${c_final} (Esperado: $11500.0)")

    # 3. Prueba de Descuento
    # Ejemplo: Prenda de $80 con el 20% de descuento
    precio_rebajado = calcular_descuento(80, 20)
    print(f"Precio con descuento: ${precio_rebajado} (Esperado: $64.0)")
