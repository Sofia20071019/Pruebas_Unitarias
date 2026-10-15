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
