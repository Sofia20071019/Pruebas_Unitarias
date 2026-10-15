"""================================================================================
ejercicio_09: Verificación de Palíndromos

Función que determina si una palabra o frase se lee igual hacia adelante que hacia atrás, ignorando mayúsculas/minúsculas y espacios. Retorna False si está vacía o solo tiene espacios.

Parte 1: Enunciado de la solución (según la guía del taller)
Parte 2: Código que resuelve la solución
Parte 3: Pruebas unitarias (en src/tests/test_ejercicio_09.py)
================================================================================

"""

def es_palindromo(cadena):
    if not isinstance(cadena, str):
        raise TypeError("El parámetro debe ser una cadena de texto")

    limpia = "".join(cadena.split()).lower()

    if len(limpia) == 0:
        return False

    return limpia == limpia[::-1]
