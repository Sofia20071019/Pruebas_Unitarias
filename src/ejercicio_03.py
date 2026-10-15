"""================================================================================
ejercicio_03: Conversión de Celsius a Fahrenheit

Función que transforma una temperatura en grados Celsius a Fahrenheit usando F = (celsius * 1.8) + 32. Rechaza temperaturas por debajo del cero absoluto (-273.15 °C) con ValueError.

Parte 1: Enunciado de la solución (según la guía del taller)
Parte 2: Código que resuelve la solución
Parte 3: Pruebas unitarias (en src/tests/test_ejercicio_03.py)
================================================================================

"""


def celsius_a_fahrenheit(celsius):
    if type(celsius) not in (int, float):
        raise TypeError("La temperatura debe ser un número")
    if celsius < -273.15:
        raise ValueError("Temperatura por debajo del cero absoluto (-273.15 °C)")
    return (celsius * 1.8) + 32
