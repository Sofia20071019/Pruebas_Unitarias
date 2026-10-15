
def es_mayor_de_edad(edad):
    if type(edad) is not int:
        raise TypeError("La edad debe ser un número entero")
    if edad < 0 or edad > 125:
        raise ValueError("La edad ingresada está fuera del rango biológico admisible [0 - 125]")
    return edad >= 18
