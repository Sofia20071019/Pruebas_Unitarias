def procesar_usuario(datos_usuario):
    if not isinstance(datos_usuario, dict):
        raise TypeError("El parámetro debe ser un diccionario")

    claves_requeridas = {"id", "nombre", "activo"}

    if not claves_requeridas.issubset(datos_usuario.keys()):
        faltantes = claves_requeridas - datos_usuario.keys()
        raise ValueError(f"Faltan campos requeridos en el registro: {faltantes}")

    if type(datos_usuario["id"]) is not int or datos_usuario["id"] <= 0:
        raise ValueError("El id debe ser un entero positivo mayor a cero")

    if (
        not isinstance(datos_usuario["nombre"], str)
        or len(datos_usuario["nombre"].strip()) == 0
    ):
        raise ValueError("El nombre debe ser una cadena no vacía")

    if type(datos_usuario["activo"]) is not bool:
        raise ValueError("El campo activo debe ser un valor booleano")

    nuevo_registro = datos_usuario.copy()
    nuevo_registro["estado_registro"] = "VALIDADO"

    return nuevo_registro
