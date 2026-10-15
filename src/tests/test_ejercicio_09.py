"""ejercicio9: Verificación de Palíndromos"""

import pytest
from src.ejercicio_09 import es_palindromo


def test_palabra_palindroma():
    cadena, esperado = "radar", True
    resultado = es_palindromo(cadena)
    assert resultado is esperado


def test_frase_con_espacios_y_mayusculas():
    cadena, esperado = "Anita lava la tina", True
    resultado = es_palindromo(cadena)
    assert resultado is esperado


def test_palabra_no_palindroma():
    cadena, esperado = "software", False
    resultado = es_palindromo(cadena)
    assert resultado is esperado


def test_solo_espacios_es_false():
    cadena, esperado = " ", False
    resultado = es_palindromo(cadena)
    assert resultado is esperado


def test_numero_lanza_typeerror():
    cadena = 1001
    with pytest.raises(TypeError):
        es_palindromo(cadena)
