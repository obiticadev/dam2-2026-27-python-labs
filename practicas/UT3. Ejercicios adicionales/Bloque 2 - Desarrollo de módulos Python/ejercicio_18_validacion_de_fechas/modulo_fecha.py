"""Ejercicio 18: Módulo de validación de fechas.

Crea las funciones es_fecha_valida(dia, mes), es_bisiesto(anio), aplicando la
regla del calendario gregoriano, y
edad_en_anios(anio_nacimiento, anio_actual). Añade un bloque de pruebas
protegido con if __name__ == "__main__":.
"""


def es_fecha_valida(dia: int, mes: int) -> bool:
    # 1. Validar que el mes sea correcto (de enero a diciembre)
    if mes < 1 or mes > 12:
        return False

    # 2. Mapear la cantidad de días que tiene cada mes
    # Clave: número de mes, Valor: cantidad máxima de días
    dias_por_mes = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    # 3. Validar que el día esté entre 1 y el máximo permitido para ese mes
    if dia < 1 or dia > dias_por_mes[mes]:
        return False

    return True


def es_bisiesto(anio: int) -> bool:
    if anio % 4 == 0 and anio % 100 != 0:
        return True
    return False


def edad_en_anios(anio_nacimiento: int, anio_actual: int) -> int:
    return anio_actual - anio_nacimiento


if __name__ == "__main__":
    dia = 10
    dia2 = 35
    mes = 12
    anio = 1950
    anio_nacimiento = 1997
    anio_actual = 2030

    print(es_fecha_valida(dia, mes))
    print(es_fecha_valida(dia2, mes))
    print(es_bisiesto(anio))
    print(edad_en_anios(anio_nacimiento, anio_actual))
