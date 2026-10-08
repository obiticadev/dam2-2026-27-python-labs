"""Ejercicio 6: Saludo personalizado multiidioma.

Codifica una función saludo_personalizado(nombre, idioma="es"), con un
parámetro por defecto, que devuelva un saludo con el nombre recibido en
español, inglés o francés según el código de idioma indicado.
"""


def saludo_personalizado(nombre: str, idioma="es") -> str:
    match idioma:
        case "es":
            return f"Hola {nombre}"
        case "en":
            return f"Hi {nombre}"


while True:
    nombre = input("\nIntroduce un nombre: ")
    print(saludo_personalizado(nombre, "en"))
