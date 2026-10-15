"""ejercicio2: Número Par o Impar"""


def es_par(numero):
    if type(numero) is not int:
        raise TypeError("El parámetro debe ser un número entero")
    return numero % 2 == 0
