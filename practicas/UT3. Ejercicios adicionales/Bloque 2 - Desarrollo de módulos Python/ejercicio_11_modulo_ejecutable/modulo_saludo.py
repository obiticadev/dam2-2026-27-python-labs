"""Ejercicio 11: Módulo ejecutable con bloque if __name__ == "__main__".

Crea dos funciones: saludar(nombre) y despedir(nombre). Al final del archivo,
añade un bloque de prueba protegido con if __name__ == "__main__": que pruebe
ambas funciones y solo se ejecute al ejecutar este módulo directamente.
"""


def saludar(nombre: str) -> str:
    return f"Hola {nombre}"


def despedir(nombre: str) -> str:
    return f"Adios {nombre}"


if __name__ == "__main__":
    print("Este mensaje SOLO aparece si se ejecuta este archivo directamente.")
    print(saludar("modo de prueba"))
    print(despedir("modo de prueba"))
