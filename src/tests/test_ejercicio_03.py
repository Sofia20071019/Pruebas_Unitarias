"""================================================================================
ejercicio_03: Conversión de Celsius a Fahrenheit

Función que transforma una temperatura en grados Celsius a Fahrenheit usando F = (celsius * 1.8) + 32. Rechaza temperaturas por debajo del cero absoluto (-273.15 °C) con ValueError.

Parte 1: Enunciado de la solución (según la guía del taller)
Parte 2: Código que resuelve la solución
Parte 3: Pruebas unitarias (en src/tests/test_ejercicio_03.py)
================================================================================

"""

import pytest
from src.ejercicio_03 import celsius_a_fahrenheit

def test_punto_congelacion():
    celsius, esperado = 0, 32.0
    resultado = celsius_a_fahrenheit(celsius)
    assert resultado == esperado


def test_punto_ebullicion():
    celsius, esperado = 100, 212.0
    resultado = celsius_a_fahrenheit(celsius)
    assert resultado == esperado


def test_escalas_coinciden():
    celsius, esperado = -40, -40.0
    resultado = celsius_a_fahrenheit(celsius)
    assert resultado == esperado


def test_temperatura_corporal_con_approx():
    celsius, esperado = 37, 98.6
    resultado = celsius_a_fahrenheit(celsius)
    assert resultado == pytest.approx(esperado)


def test_bajo_cero_absoluto_lanza_valueerror():
    celsius = -273.16
    with pytest.raises(ValueError):
        celsius_a_fahrenheit(celsius)