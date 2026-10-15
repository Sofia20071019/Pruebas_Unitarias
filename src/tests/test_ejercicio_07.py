"""ejercicio7: Cálculo del Factorial"""

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
