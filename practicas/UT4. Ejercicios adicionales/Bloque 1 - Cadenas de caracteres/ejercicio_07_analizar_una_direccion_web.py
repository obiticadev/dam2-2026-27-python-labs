"""Ejercicio 7: Analizar una dirección web.

Nivel: Medio.

Enunciado: Una dirección web tiene la forma protocolo://dominio/ruta?parametros, por
ejemplo https://www.ejemplo.es/tienda/producto?id=42&color=rojo. Escribe las funciones:

- analizar_url(url), que devuelva una tupla (protocolo, dominio, ruta, consulta) (usa
  .split("://"), .find() y slicing; si no hay ruta, esta será "/", y si no hay
  parámetros, la consulta será una cadena vacía);

- es_segura(url), que devuelva True si la dirección empieza por https://;

- y obtener_parametros(consulta), que convierta una consulta como "id=42&color=rojo" en
  un diccionario {"id": "42", "color": "rojo"} (separa primero por & y después cada
  pareja por =).

Prueba las funciones con la dirección de ejemplo y con http://localhost.
"""
