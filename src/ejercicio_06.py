"""================================================================================
ejercicio_06: Longitud de Contraseña

Función que determina si una contraseña cumple con el criterio de seguridad de longitud mínima y máxima (entre 8 y 20 caracteres inclusive). Lanza TypeError si no es cadena.

Parte 1: Enunciado de la solución (según la guía del taller)
Parte 2: Código que resuelve la solución
Parte 3: Pruebas unitarias (en src/tests/test_ejercicio_06.py)
================================================================================

"""


def validar_longitud_password(password):
    if not isinstance(password, str):
        raise TypeError("El password debe ser una cadena de caracteres")
    return 8 <= len(password) <= 20
