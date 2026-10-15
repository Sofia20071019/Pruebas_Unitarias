"""================================================================================
ejercicio_08: Obtener el Número Mayor de una Lista

Función que recibe una lista de números y devuelve el valor más alto sin usar la función nativa max(). Valida que sea lista, no vacía y que todos los elementos sean numéricos.

Parte 1: Enunciado de la solución (según la guía del taller)
Parte 2: Código que resuelve la solución
Parte 3: Pruebas unitarias (en src/tests/test_ejercicio_08.py)
================================================================================

"""

def obtener_mayor(lista_numeros):
    if not isinstance(lista_numeros, list):
        raise TypeError("El argumento debe ser una lista")
    if len(lista_numeros) == 0:
        raise ValueError("La lista no puede estar vacía")

    mayor = lista_numeros[0]

    for elemento in lista_numeros:
        if type(elemento) not in (int, float):
            raise TypeError("Todos los elementos de la lista deben ser números")
        if elemento > mayor:
            mayor = elemento

    return mayor
