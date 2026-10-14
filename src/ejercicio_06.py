import pytest
from src.ejercicio_06 import validar_longitud_password

def validar_longitud_password(password):
    if not isinstance(password, str):
        raise TypeError("El password debe ser una cadena de caracteres")
    return 8 <= len(password) <= 20
