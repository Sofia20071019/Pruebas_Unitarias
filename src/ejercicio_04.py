"""================================================================================
ejercicio_04: Cálculo de Descuento Comercial

Función que devuelve el precio final tras aplicar un porcentaje de descuento. Valida que precio >= 0 y que el descuento esté entre 0 y 100 inclusive, rechazando no numéricos y booleanos.

Parte 1: Enunciado de la solución (según la guía del taller)
Parte 2: Código que resuelve la solución
Parte 3: Pruebas unitarias (en src/tests/test_ejercicio_04.py)
================================================================================

"""


def aplicar_descuento(precio, porcentaje_descuento):
    if not (isinstance(precio, (int, float)) and isinstance(porcentaje_descuento, (int, float))):
        raise TypeError("Los valores deben ser numéricos")
    if isinstance(precio, bool) or isinstance(porcentaje_descuento, bool):
        raise TypeError("Los valores no pueden ser booleanos")
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if porcentaje_descuento < 0 or porcentaje_descuento > 100:
        raise ValueError("El descuento debe estar entre 0 y 100")

    descuento = precio * (porcentaje_descuento / 100)
    return precio - descuento