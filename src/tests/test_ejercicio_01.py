"""================================================================================
ejercicio_01: Suma Segura de Dos Números

Función que suma dos números estrictamente numéricos (int o float), rechazando booleanos explícitamente. Lanza TypeError si recibe un argumento inválido.

Parte 1: Enunciado de la solución (según la guía del taller)
Parte 2: Código que resuelve la solución
Parte 3: Pruebas unitarias (en src/tests/test_ejercicio_01.py)
================================================================================

"""

import pytest 
from src.ejercicio_01 import sumar

def test_suma_enteros_positivos():
    a, b, esperado = 2, 3, 5
    resultado = sumar(a, b)    
    assert resultado == esperado

def test_suma_positivo_y_negativo():
    a, b, esperado = 10, -4, 6
    resultado = sumar(a, b)
    assert resultado == esperado

def test_string_lanza_typeerror():
    a, b = "5", 3
    with pytest.raises(TypeError):
        sumar(a, b)

def test_booleano_lanza_typeerror():
    a, b = True, 3
    with pytest.raises(TypeError):
        sumar(a, b)