"""================================================================================
ejercicio_11: División Segura

Función que efectúa la operación de división devolviendo el resultado como float. Lanza explícitamente ZeroDivisionError si el divisor es 0 y TypeError si algún operando no es numérico.

Parte 1: Enunciado de la solución (según la guía del taller)
Parte 2: Código que resuelve la solución
Parte 3: Pruebas unitarias (en src/tests/test_ejercicio_11.py)
================================================================================

"""

def division_segura(dividendo, divisor):
    if type(dividendo) not in (int, float) or type(divisor) not in (int, float):
        raise TypeError("Los operandos deben ser numéricos")
    if divisor == 0:
        raise ZeroDivisionError("No es posible dividir entre cero")

    return dividendo / divisor
