"""================================================================================
ejercicio_07: Cálculo del Factorial

Función que calcula el factorial de un número entero no negativo (n!). 0! = 1 y 1! = 1. Lanza ValueError para negativos y TypeError si no es entero.

Parte 1: Enunciado de la solución (según la guía del taller)
Parte 2: Código que resuelve la solución
Parte 3: Pruebas unitarias (en src/tests/test_ejercicio_07.py)
================================================================================

"""

import pytest
from src.ejercicio_07 import factorial


def test_factorial_de_0():
    n, esperado = 0, 1
    resultado = factorial(n)
    assert resultado == esperado


def test_factorial_de_1():
    n, esperado = 1, 1
    resultado = factorial(n)
    assert resultado == esperado


def test_factorial_de_5():
    n, esperado = 5, 120
    resultado = factorial(n)
    assert resultado == esperado


def test_factorial_de_7():
    n, esperado = 7, 5040
    resultado = factorial(n)
    assert resultado == esperado


def test_factorial_negativo_lanza_valueerror():
    n = -3
    with pytest.raises(ValueError):
        factorial(n)
