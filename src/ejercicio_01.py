import pytest
from src.ejercicio_01 import sumar

def sumar(a, b):
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("Ambos argumentos deben ser estrictamente numéricos (int o float)")
    return a + b