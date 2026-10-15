"""================================================================================
ejercicio_02: Número Par o Impar

Función que determina si un número entero es par o impar. Rechaza cualquier valor que no sea exactamente int (incluye decimales como 4.0) con TypeError.

Parte 1: Enunciado de la solución (según la guía del taller)
Parte 2: Código que resuelve la solución
Parte 3: Pruebas unitarias (en src/tests/test_ejercicio_02.py)
================================================================================

"""

import pytest
from src.ejercicio_02 import es_par

def test_par_positivo():
    numero, esperado = 8, True
    resultado = es_par(numero)
    assert resultado is esperado


def test_impar_positivo():
    numero, esperado = 7, False
    resultado = es_par(numero)
    assert resultado is esperado


def test_cero_es_par():
    numero, esperado = 0, True
    resultado = es_par(numero)
    assert resultado is esperado


def test_par_negativo():
    numero, esperado = -4, True
    resultado = es_par(numero)
    assert resultado is esperado


def test_impar_negativo():
    numero, esperado = -9, False
    resultado = es_par(numero)
    assert resultado is esperado


def test_decimal_lanza_typeerror():
    numero = 4.0
    with pytest.raises(TypeError):
        es_par(numero)