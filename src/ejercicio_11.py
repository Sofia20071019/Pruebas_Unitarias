"""ejercicio11: División Segura"""

def division_segura(dividendo, divisor):
    if type(dividendo) not in (int, float) or type(divisor) not in (int, float):
        raise TypeError("Los operandos deben ser numéricos")
    if divisor == 0:
        raise ZeroDivisionError("No es posible dividir entre cero")

    return dividendo / divisor
