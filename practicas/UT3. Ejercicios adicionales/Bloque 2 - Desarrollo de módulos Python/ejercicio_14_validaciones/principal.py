"""Programa principal del ejercicio 14.

Importa el módulo con el alias indicado:

    import validaciones as val

Usa desde aquí sus tres funciones de validación.
"""
import validaciones as val

email = "example23@gmail.com"
tlf = "999999999"
password = "Edfdfdf899"

print(
    f"El método {val.es_email_valido.__qualname__} con {email} de texto es igual a {val.es_email_valido(email)}")
print(
    f"El método {val.es_telefono_valido.__qualname__} con {tlf} de texto es igual a {val.es_telefono_valido(tlf)}")
print(
    f"El método {val.es_contrasena_segura.__qualname__} con {password} de texto es igual a {val.es_contrasena_segura(password)}")
