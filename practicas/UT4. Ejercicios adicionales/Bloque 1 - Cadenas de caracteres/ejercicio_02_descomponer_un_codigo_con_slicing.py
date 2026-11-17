"""Ejercicio 2: Descomponer un código con slicing.

Nivel: Básico.

Enunciado: Los códigos de los productos de una tienda tienen siempre el formato
PP-AAAA-NNNNN-T: dos letras de país, cuatro cifras de año, cinco cifras de número de
serie y la talla (una o dos letras), separados por guiones; por ejemplo,
"ES-2026-00457-XL".

Escribe una función describir_codigo(codigo) que, usando solo slicing (sin .split()),
devuelva un texto como "País: ES | Año: 2026 | Serie: 457 | Talla: XL" (el número de
serie debe mostrarse sin ceros a la izquierda). Muestra además, para el mismo código,
sus dos últimos caracteres y el código invertido.
"""
