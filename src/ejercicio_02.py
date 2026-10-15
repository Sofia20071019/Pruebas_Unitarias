"""================================================================================
ejercicio_02: Número Par o Impar

Función que determina si un número entero es par o impar. Rechaza cualquier valor que no sea exactamente int (incluye decimales como 4.0) con TypeError.

Parte 1: Enunciado de la solución (según la guía del taller)
Parte 2: Código que resuelve la solución
Parte 3: Pruebas unitarias (en src/tests/test_ejercicio_02.py)
================================================================================

"""


def es_par(numero):
    if type(numero) is not int:
        raise TypeError("El parámetro debe ser un número entero")
    return numero % 2 == 0
