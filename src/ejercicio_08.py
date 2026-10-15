"""ejercicio8: Obtener el Número Mayor de una Lista"""

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
