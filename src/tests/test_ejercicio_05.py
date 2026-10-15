"""ejercicio5: Verificación de Mayoría de Edad"""

import pytest
from src.ejercicio_05 import es_mayor_de_edad

def test_17_no_es_mayor():
    edad, esperado = 17, False
    resultado = es_mayor_de_edad(edad)
    assert resultado is esperado


def test_18_es_mayor():
    edad, esperado = 18, True
    resultado = es_mayor_de_edad(edad)
    assert resultado is esperado


def test_19_es_mayor():
    edad, esperado = 19, True
    resultado = es_mayor_de_edad(edad)
    assert resultado is esperado


def test_edad_negativa_lanza_valueerror():
    edad = -1
    with pytest.raises(ValueError):
        es_mayor_de_edad(edad)


def test_edad_126_lanza_valueerror():
    edad = 126
    with pytest.raises(ValueError):
        es_mayor_de_edad(edad)