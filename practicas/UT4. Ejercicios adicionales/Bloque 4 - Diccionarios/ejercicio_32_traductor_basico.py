"""Ejercicio 32: Traductor básico.

Nivel: Básico.

Enunciado: Un diccionario asocia palabras en español con su traducción al inglés:
DICCIONARIO = {"hola": "hello", "mundo": "world", "gato": "cat", "perro": "dog", "casa":
"house", "grande": "big", "el": "the", "la": "the", "es": "is"}. Escribe:

- traducir_palabra(palabra), que devuelva la traducción de una palabra (sin distinguir
  mayúsculas) o la propia palabra entre corchetes con un signo de interrogación
  ("[azul?]") si no está en el diccionario;

- traducir_frase(frase), que traduzca una frase palabra a palabra con .split() y "
  ".join();

- y anadir_traduccion(espanol, ingles), que añada una entrada nueva.

Traduce "el gato es grande" y "la casa es azul", añade la traducción de "azul" y vuelve
a traducir la segunda frase. Muestra por último las palabras del diccionario ordenadas
alfabéticamente.
"""
