"""================================================================================
ejercicio_05: Verificación de Mayoría de Edad

Función que recibe una edad en años (entero) y retorna True si es mayor o igual a 18, False en caso contrario. Valida rango biológico [0 - 125] y tipo entero.

Parte 1: Enunciado de la solución (según la guía del taller)
Parte 2: Código que resuelve la solución
Parte 3: Pruebas unitarias (en src/tests/test_ejercicio_05.py)
================================================================================

"""


def es_mayor_de_edad(edad):
    if type(edad) is not int:
        raise TypeError("La edad debe ser un número entero")
    if edad < 0 or edad > 125:
        raise ValueError("La edad ingresada está fuera del rango biológico admisible [0 - 125]")
    return edad >= 18
