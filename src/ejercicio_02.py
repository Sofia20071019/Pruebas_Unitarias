import pytest
from src.ejercicio_02 import es_par

def es_par(numero):
    if type(numero) is not int:
        raise TypeError("El parámetro debe ser un número entero")
    return numero % 2 == 0
