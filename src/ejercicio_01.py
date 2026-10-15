"""================================================================================
ejercicio_01: Suma Segura de Dos Números

Función que suma dos números estrictamente numéricos (int o float), rechazando booleanos explícitamente. Lanza TypeError si recibe un argumento inválido.

Parte 1: Enunciado de la solución (según la guía del taller)
Parte 2: Código que resuelve la solución
Parte 3: Pruebas unitarias (en src/tests/test_ejercicio_01.py)
================================================================================

"""

def sumar(a, b):
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("Ambos argumentos deben ser estrictamente numéricos (int o float)")
    return a + b