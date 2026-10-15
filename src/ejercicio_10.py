"""================================================================================
ejercicio_10: Clasificación de Calificaciones SENA

Función que devuelve la descripción cualitativa del desempeño académico sobre una escala de 0.0 a 5.0 (Excelente, Bueno, Aceptable, Deficiente). Lanza ValueError fuera de escala.

Parte 1: Enunciado de la solución (según la guía del taller)
Parte 2: Código que resuelve la solución
Parte 3: Pruebas unitarias (en src/tests/test_ejercicio_10.py)
================================================================================

"""

def clasificar_nota(nota):
    if type(nota) not in (int, float):
        raise TypeError("La nota debe ser un número flotante o entero")
    if nota < 0.0 or nota > 5.0:
        raise ValueError("Nota fuera de la escala [0.0 - 5.0]")

    if nota >= 4.5:
        return "Excelente"
    elif nota >= 3.5:
        return "Bueno"
    elif nota >= 3.0:
        return "Aceptable"
    else:
        return "Deficiente"
