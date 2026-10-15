"""================================================================================
ejercicio_07: Cálculo del Factorial

Función que calcula el factorial de un número entero no negativo (n!). 0! = 1 y 1! = 1. Lanza ValueError para negativos y TypeError si no es entero.

Parte 1: Enunciado de la solución (según la guía del taller)
Parte 2: Código que resuelve la solución
Parte 3: Pruebas unitarias (en src/tests/test_ejercicio_07.py)
================================================================================

"""

def factorial(n):
    if type(n) is not int:
        raise TypeError("El argumento debe ser un número entero")
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")

    resultado = 1
    for i in range(2, n + 1):
        resultado *= i

    return resultado
