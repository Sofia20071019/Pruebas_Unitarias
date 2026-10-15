"""ejercicio4: Cálculo de Descuento Comercial"""


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