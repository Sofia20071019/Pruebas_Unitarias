"""ejercicio2: Número Par o Impar"""

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