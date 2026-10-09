"""Ejercicio 14: Módulo de validación de correos electrónicos.

Crea estas funciones:

- es_email_valido(texto): comprueba que contiene un "@" y un ".".
- es_telefono_valido(texto): comprueba con .isdigit() que tiene 9 dígitos.
- es_contrasena_segura(texto): comprueba que tiene al menos 8 caracteres.

Añade un bloque de pruebas protegido con if __name__ == "__main__":.
"""


def es_email_valido(texto: str) -> bool:
    return "@" in texto and "." in texto


def es_telefono_valido(texto: str) -> bool:
    return texto.isdigit() and len(texto) == 9


def es_contrasena_segura(texto: str) -> bool:
    return len(texto) >= 8


if __name__ == "__main__":
    email = "example@gmail.com"
    tlf = "600520459"
    password = "Estric899"
    print(
        f"El método {es_email_valido.__qualname__} con {email} de texto es igual a {es_email_valido(email)}")
    print(
        f"El método {es_telefono_valido.__qualname__} con {tlf} de texto es igual a {es_telefono_valido(tlf)}")
    print(
        f"El método {es_contrasena_segura.__qualname__} con {password} de texto es igual a {es_contrasena_segura(password)}")
