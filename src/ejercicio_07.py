"""ejercicio7: Cálculo del Factorial"""

def factorial(n):
    if type(n) is not int:
        raise TypeError("El argumento debe ser un número entero")
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")

    resultado = 1
    for i in range(2, n + 1):
        resultado *= i

    return resultado
