"""================================================================================
ejercicio_06: Longitud de Contraseña

Función que determina si una contraseña cumple con el criterio de seguridad de longitud mínima y máxima (entre 8 y 20 caracteres inclusive). Lanza TypeError si no es cadena.

Parte 1: Enunciado de la solución (según la guía del taller)
Parte 2: Código que resuelve la solución
Parte 3: Pruebas unitarias (en src/tests/test_ejercicio_06.py)
================================================================================

"""

import pytest 
from src.ejercicio_06 import validar_longitud_password

def test_longitud_7_es_invalida():
    password, esperado = "a" * 7, False
    resultado = validar_longitud_password(password)
    assert resultado is esperado


def test_longitud_8_es_valida():
    password, esperado = "a" * 8, True
    resultado = validar_longitud_password(password)
    assert resultado is esperado


def test_longitud_20_es_valida():
    password, esperado = "a" * 20, True
    resultado = validar_longitud_password(password)
    assert resultado is esperado


def test_longitud_21_es_invalida():
    password, esperado = "a" * 21, False
    resultado = validar_longitud_password(password)
    assert resultado is esperado


def test_none_lanza_typeerror():
    password = None
    with pytest.raises(TypeError):
        validar_longitud_password(password)


def test_numero_lanza_typeerror():
    password = 12345678
    with pytest.raises(TypeError):
        validar_longitud_password(password)