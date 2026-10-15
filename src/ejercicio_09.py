def es_palindromo(cadena):
    if not isinstance(cadena, str):
        raise TypeError("El parámetro debe ser una cadena de texto")

    limpia = "".join(cadena.split()).lower()

    if len(limpia) == 0:
        return False

    return limpia == limpia[::-1]
