"""ejercicio3: Conversión de Celsius a Fahrenheit"""

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