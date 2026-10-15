"""================================================================================
ejercicio_08: Obtener el Número Mayor de una Lista

Función que recibe una lista de números y devuelve el valor más alto sin usar la función nativa max(). Valida que sea lista, no vacía y que todos los elementos sean numéricos.

Parte 1: Enunciado de la solución (según la guía del taller)
Parte 2: Código que resuelve la solución
Parte 3: Pruebas unitarias (en src/tests/test_ejercicio_08.py)
================================================================================

"""

import pytest
from src.ejercicio_08 import obtener_mayor


def test_mayor_en_lista_desordenada():
    lista, esperado = [4, 12, 8, 3], 12
    resultado = obtener_mayor(lista)
    assert resultado == esperado


def test_mayor_con_negativos():
    lista, esperado = [-15, -3, -8, -20], -3
    resultado = obtener_mayor(lista)
    assert resultado == esperado


def test_lista_de_un_elemento():
    lista, esperado = [42], 42
    resultado = obtener_mayor(lista)
    assert resultado == esperado


def test_lista_vacia_lanza_valueerror():
    lista = []
    with pytest.raises(ValueError):
        obtener_mayor(lista)


def test_elemento_no_numerico_lanza_typeerror():
    lista = [1, 2, "tres"]
    with pytest.raises(TypeError):
        obtener_mayor(lista)
