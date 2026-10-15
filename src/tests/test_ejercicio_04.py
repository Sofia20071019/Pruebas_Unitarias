"""================================================================================
ejercicio_04: Cálculo de Descuento Comercial

Función que devuelve el precio final tras aplicar un porcentaje de descuento. Valida que precio >= 0 y que el descuento esté entre 0 y 100 inclusive, rechazando no numéricos y booleanos.

Parte 1: Enunciado de la solución (según la guía del taller)
Parte 2: Código que resuelve la solución
Parte 3: Pruebas unitarias (en src/tests/test_ejercicio_04.py)
================================================================================

"""

import pytest
from src.ejercicio_04 import aplicar_descuento

def test_descuento_general():
    precio, descuento, esperado = 100000, 20, 80000.0
    resultado = aplicar_descuento(precio, descuento)
    assert resultado == esperado


def test_descuento_cero():
    precio, descuento, esperado = 50000, 0, 50000.0
    resultado = aplicar_descuento(precio, descuento)
    assert resultado == esperado


def test_descuento_cien():
    precio, descuento, esperado = 75000, 100, 0.0
    resultado = aplicar_descuento(precio, descuento)
    assert resultado == esperado


def test_descuento_menor_a_cero_lanza_valueerror():
    precio, descuento = 1000, -1
    with pytest.raises(ValueError):
        aplicar_descuento(precio, descuento)


def test_descuento_mayor_a_cien_lanza_valueerror():
    precio, descuento = 1000, 101
    with pytest.raises(ValueError):
        aplicar_descuento(precio, descuento)