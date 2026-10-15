import pytest
from src.ejercicio_10 import clasificar_nota


def test_nota_maxima_5_0_es_excelente():
    nota, esperado = 5.0, "Excelente"
    resultado = clasificar_nota(nota)
    assert resultado == esperado


def test_nota_4_5_es_excelente():
    nota, esperado = 4.5, "Excelente"
    resultado = clasificar_nota(nota)
    assert resultado == esperado


def test_nota_4_4_es_bueno():
    nota, esperado = 4.4, "Bueno"
    resultado = clasificar_nota(nota)
    assert resultado == esperado


def test_nota_3_0_es_aceptable():
    nota, esperado = 3.0, "Aceptable"
    resultado = clasificar_nota(nota)
    assert resultado == esperado


def test_nota_2_9_es_deficiente():
    nota, esperado = 2.9, "Deficiente"
    resultado = clasificar_nota(nota)
    assert resultado == esperado


def test_nota_0_0_es_deficiente():
    nota, esperado = 0.0, "Deficiente"
    resultado = clasificar_nota(nota)
    assert resultado == esperado


def test_nota_menor_a_cero_lanza_valueerror():
    nota = -0.1
    with pytest.raises(ValueError):
        clasificar_nota(nota)


def test_nota_mayor_a_cinco_lanza_valueerror():
    nota = 5.1
    with pytest.raises(ValueError):
        clasificar_nota(nota)


def test_nota_no_numerica_lanza_typeerror():
    nota = "4.5"
    with pytest.raises(TypeError):
        clasificar_nota(nota)
