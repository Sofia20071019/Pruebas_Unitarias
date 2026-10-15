import pytest
from src.ejercicio_11 import division_segura


def test_division_exacta():
    dividendo, divisor, esperado = 10, 2, 5.0
    resultado = division_segura(dividendo, divisor)
    assert resultado == esperado


def test_division_periodica_con_aproximacion():
    dividendo, divisor = 10, 3
    resultado = division_segura(dividendo, divisor)
    assert resultado == pytest.approx(3.3333333333333335)


def test_cero_en_dividendo():
    dividendo, divisor, esperado = 0, 5, 0.0
    resultado = division_segura(dividendo, divisor)
    assert resultado == esperado


def test_division_por_cero_lanza_zerodivisionerror():
    dividendo, divisor = 8, 0
    with pytest.raises(ZeroDivisionError):
        division_segura(dividendo, divisor)


def test_operando_no_numerico_lanza_typeerror():
    dividendo, divisor = "10", 2
    with pytest.raises(TypeError):
        division_segura(dividendo, divisor)
