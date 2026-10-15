"""ejercicio12: Validación de Diccionario de Usuario"""

import pytest
from src.ejercicio_12 import procesar_usuario


def test_caso_exitoso_retorna_diccionario_validado():
    datos_usuario = {"id": 1, "nombre": "Ana Sofia", "activo": True}
    esperado = {"id": 1, "nombre": "Ana Sofia", "activo": True, "estado_registro": "VALIDADO"}
    resultado = procesar_usuario(datos_usuario)
    assert resultado == esperado
    assert resultado["estado_registro"] == "VALIDADO"
    assert "id" in resultado
    assert "nombre" in resultado
    assert "activo" in resultado


def test_clave_faltante_lanza_valueerror():
    datos_usuario = {"id": 1, "nombre": "Ana Sofia"}
    with pytest.raises(ValueError):
        procesar_usuario(datos_usuario)


def test_id_cero_o_negativo_lanza_valueerror():
    for datos_usuario in [
        {"id": 0, "nombre": "Ana", "activo": True},
        {"id": -5, "nombre": "Ana", "activo": True},
    ]:
        with pytest.raises(ValueError):
            procesar_usuario(datos_usuario)


def test_nombre_vacio_o_solo_espacios_lanza_valueerror():
    for datos_usuario in [
        {"id": 1, "nombre": "", "activo": True},
        {"id": 1, "nombre": "   ", "activo": True},
    ]:
        with pytest.raises(ValueError):
            procesar_usuario(datos_usuario)


def test_argumento_no_es_diccionario_lanza_typeerror():
    datos_usuario = [1, "Ana", True]
    with pytest.raises(TypeError):
        procesar_usuario(datos_usuario)
