# Documentación de Pruebas Unitarias — Taller I

**Proyecto:** Taller de Pruebas Unitarias I (Guía del Aprendiz)  
**Competencia:** Implementar la solución de software de acuerdo con los requisitos y el diseño (Fase de Evaluación / Pruebas)  
**Framework:** `pytest` (Python 3.10+)  
**Estado:** 12 ejercicios implementados + 65 pruebas unitarias — **todas pasando**

---

## 1. Objetivo del documento

Explicar de forma clara:

* Qué se implementó en cada uno de los 12 ejercicios.
* Cómo funcionan las pruebas unitarias diseñadas (qué validan y con qué técnica).
* Cómo ejecutar las pruebas desde cero en tu máquina.

Este documento acompaña la entrega del repositorio y puede leerse como guía de uso y como evidencia del taller.

---

## 2. Estructura del proyecto (obligatoria según la guía)

```
taller-pruebas-unitarias/
├── .gitignore
├── requirements.txt
├── README.md
├── DOCUMENTACION_PRUEBAS_UNITARIAS.md   <-- este archivo
└── src/
    ├── __init__.py
    ├── ejercicio_01.py          # sumar(a, b)
    ├── ejercicio_02.py          # es_par(numero)
    ├── ejercicio_03.py          # celsius_a_fahrenheit(celsius)
    ├── ejercicio_04.py          # aplicar_descuento(precio, porcentaje_descuento)
    ├── ejercicio_05.py          # es_mayor_de_edad(edad)
    ├── ejercicio_06.py          # validar_longitud_password(password)
    ├── ejercicio_07.py          # factorial(n)
    ├── ejercicio_08.py          # obtener_mayor(lista_numeros)
    ├── ejercicio_09.py          # es_palindromo(cadena)
    ├── ejercicio_10.py          # clasificar_nota(nota)
    ├── ejercicio_11.py          # division_segura(dividendo, divisor)
    ├── ejercicio_12.py          # procesar_usuario(datos_usuario)
    └── tests/
        ├── __init__.py
        ├── test_ejercicio_01.py
        ├── test_ejercicio_02.py
        ├── test_ejercicio_03.py
        ├── test_ejercicio_04.py
        ├── test_ejercicio_05.py
        ├── test_ejercicio_06.py
        ├── test_ejercicio_07.py
        ├── test_ejercicio_08.py
        ├── test_ejercicio_09.py
        ├── test_ejercicio_10.py
        ├── test_ejercicio_11.py
        └── test_ejercicio_12.py
```

*Cada función vive en su archivo independiente dentro de `src/`.  
Cada suite de pruebas vive en `src/tests/` con el prefijo obligatorio `test_`.*

---

## 3. Patrón de diseño de pruebas: AAA (Arrange-Act-Assert)

Todas las pruebas del taller siguen estrictamente las tres fases del patrón **AAA**, como exige la guía:

| Fase | Qué se hace | Ejemplo en código |
|------|-------------|-------------------|
| **Arrange** (Preparar) | Declarar variables, datos de entrada y definir el oráculo (valor esperado). | `a, b, esperado = 2, 3, 5` |
| **Act** (Actuar) | Invocar la función bajo prueba capturando el resultado. | `resultado = sumar(a, b)` |
| **Assert** (Verificar) | Aserción determinista contra el valor exacto esperado (sin desigualdades genéricas). | `assert resultado == esperado` |

Además se aplican:

* **Análisis de Valores Límite (BVA):** probar inmediatamente inferior, el borde exacto y inmediatamente superior de una frontera crítica (ej. edad 17, 18, 19).
* **Partición de Equivalencia (EP):** probar representantes de cada clase de entrada válida e inválida (ej. nota 5.0, 4.5, 4.4, 3.0, 2.9, 0.0).
* **Manejo de excepciones:** verificar que se lanza la excepción correcta (`pytest.raises`) cuando se infringen las reglas de negocio.

---

## 4. Cómo configurar el entorno y ejecutar las pruebas

### 4.1 Requisitos previos

* Python 3.10 o superior (en este taller se usó Python 3.13.5).
* `pytest` (versión 9.1.1 según `requirements.txt`).

### 4.2 Pasos desde la terminal

Abra una terminal en la **raíz del proyecto** (donde está `requirements.txt`):

```bash
# 1. Crear entorno virtual (recomendado)
python -m venv venv

# 2. Activarlo
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# Windows (CMD):
.\venv\Scripts\activate.bat
# Linux / macOS:
source venv/bin/activate

# 3. Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# 4. Ejecutar TODAS las pruebas
python -m pytest -v

# 5. Ejecutar pruebas de un ejercicio específico
python -m pytest -v src/tests/test_ejercicio_01.py

# 6. Ver salidas por consola (print) detalladas
python -m pytest -v -s
```

### 4.3 Resultado esperado

```text
============================= 65 passed in 0.23s ==============================
```

Si todo está correcto, deben aparecer **65 passed** y cero fallos.

---

## 5. Detalle de los ejercicios y sus pruebas

A continuación se describe cada ejercicio: qué hace la función, qué reglas de negocio valida y qué pruebas unitarias se diseñaron.

### 5.1 Ejercicio 01 — Suma Segura de Dos Números

**Archivos:** `src/ejercicio_01.py`, `src/tests/test_ejercicio_01.py`

**Función:** `sumar(a, b)`  
Devuelve `a + b`. Valida que ambos argumentos sean estrictamente `int` o `float` (rechaza booleanos explícitamente, porque en Python `bool` es subclase de `int`). Lanza `TypeError` si recibe un argumento inválido.

**Pruebas diseñadas (4):**

| Caso | Entrada | Esperado | Técnica |
|------|---------|----------|---------|
| Happy Path | `sumar(2, 3)` | `5` | Suma de enteros positivos |
| Negativos | `sumar(10, -4)` | `6` | Entero positivo + negativo |
| Tipo inválido | `sumar("5", 3)` | `TypeError` | Manejo de excepción |
| Booleano | `sumar(True, 3)` | `TypeError` | Rechazo explícito de bool |

---

### 5.2 Ejercicio 02 — Número Par o Impar

**Archivos:** `src/ejercicio_02.py`, `src/tests/test_ejercicio_02.py`

**Función:** `es_par(numero)`  
Retorna `True` si el número entero es par, `False` si es impar. Rechaza cualquier valor que no sea exactamente `int` (incluye decimales como `4.0`) con `TypeError`.

**Pruebas diseñadas (6):**

| Caso | Entrada | Esperado | Técnica |
|------|---------|----------|---------|
| Par positivo | `es_par(8)` | `True` | Caso positivo |
| Impar positivo | `es_par(7)` | `False` | Caso negativo |
| Valor neutro | `es_par(0)` | `True` | 0 es matemáticamente par |
| Par negativo | `es_par(-4)` | `True` | Enteros negativos pares |
| Impar negativo | `es_par(-9)` | `False` | Enteros negativos impares |
| Decimal | `es_par(4.0)` | `TypeError` | Rechazo de no entero exacto |

---

### 5.3 Ejercicio 03 — Conversión Celsius a Fahrenheit

**Archivos:** `src/ejercicio_03.py`, `src/tests/test_ejercicio_03.py`

**Función:** `celsius_a_fahrenheit(celsius)`  
Aplica `F = (celsius * 1.8) + 32`. Rechaza temperaturas por debajo del cero absoluto (-273.15 °C) con `ValueError`. Valida que la entrada sea numérica (`int` o `float`), lanzando `TypeError` en caso contrario.

**Pruebas diseñadas (5):**

| Caso | Entrada | Esperado | Técnica |
|------|---------|----------|---------|
| Congelación agua | `celsius_a_fahrenheit(0)` | `32.0` | Punto de congelación |
| Ebullición agua | `celsius_a_fahrenheit(100)` | `212.0` | Punto de ebullición |
| Coincidencia escalas | `celsius_a_fahrenheit(-40)` | `-40.0` | -40 °C = -40 °F |
| Precisión decimal | `celsius_a_fahrenheit(37)` | `98.6` (aprox) | `pytest.approx` |
| Bajo cero absoluto | `celsius_a_fahrenheit(-273.16)` | `ValueError` | Límite inferior no permitido |

---

### 5.4 Ejercicio 04 — Cálculo de Descuento Comercial

**Archivos:** `src/ejercicio_04.py`, `src/tests/test_ejercicio_04.py`

**Función:** `aplicar_descuento(precio, porcentaje_descuento)`  
Devuelve el precio final tras aplicar el descuento. Reglas:
* `precio >= 0`.
* `0 <= porcentaje_descuento <= 100`.
* Ambos deben ser numéricos y no booleanos.
* Lanza `TypeError` o `ValueError` según corresponda.

**Pruebas diseñadas (5):**

| Caso | Entrada | Esperado | Técnica |
|------|---------|----------|---------|
| Caso general | `aplicar_descuento(100000, 20)` | `80000.0` | Descuento del 20 % |
| Límite inferior descuento | `aplicar_descuento(50000, 0)` | `50000.0` | 0 % de descuento |
| Límite superior descuento | `aplicar_descuento(75000, 100)` | `0.0` | 100 % de descuento |
| Descuento < 0 | `aplicar_descuento(1000, -1)` | `ValueError` | Fuera de rango inferior |
| Descuento > 100 | `aplicar_descuento(1000, 101)` | `ValueError` | Fuera de rango superior |

---

### 5.5 Ejercicio 05 — Verificación de Mayoría de Edad

**Archivos:** `src/ejercicio_05.py`, `src/tests/test_ejercicio_05.py`

**Función:** `es_mayor_de_edad(edad)`  
Recibe edad en años (entero). Retorna `True` si `edad >= 18`, `False` si es menor. Lanza:
* `TypeError` si `edad` no es `int`.
* `ValueError` si `edad < 0` o `edad > 125` (rango biológico admisible).

**Pruebas diseñadas (5, técnica BVA):**

| Caso | Entrada | Esperado | Técnica |
|------|---------|----------|---------|
| Inmediatamente inferior | `es_mayor_de_edad(17)` | `False` | BVA borde inferior |
| Frontera exacta | `es_mayor_de_edad(18)` | `True` | BVA frontera crítica |
| Inmediatamente superior | `es_mayor_de_edad(19)` | `True` | BVA borde superior |
| Límite biológico inferior inválido | `es_mayor_de_edad(-1)` | `ValueError` | Fuera de rango |
| Límite biológico superior inválido | `es_mayor_de_edad(126)` | `ValueError` | Fuera de rango |

---

### 5.6 Ejercicio 06 — Longitud de Contraseña

**Archivos:** `src/ejercicio_06.py`, `src/tests/test_ejercicio_06.py`

**Función:** `validar_longitud_password(password)`  
Retorna `True` si la contraseña tiene entre 8 y 20 caracteres inclusive, `False` en otro caso. Lanza `TypeError` si el argumento no es `str`.

**Pruebas diseñadas (6, enfoque en límites de caracteres):**

| Caso | Entrada | Esperado | Técnica |
|------|---------|----------|---------|
| Longitud 7 | `"a"*7` | `False` | Borde inválido inferior |
| Longitud 8 | `"a"*8` | `True` | Borde válido inferior |
| Longitud 20 | `"a"*20` | `True` | Borde válido superior |
| Longitud 21 | `"a"*21` | `False` | Borde inválido superior |
| Valor nulo | `None` | `TypeError` | Tipo no cadena |
| Valor numérico | `12345678` | `TypeError` | Tipo no cadena |

---

### 5.7 Ejercicio 07 — Cálculo del Factorial

**Archivos:** `src/ejercicio_07.py`, `src/tests/test_ejercicio_07.py`

**Función:** `factorial(n)`  
Calcula `n!` para entero no negativo. `0! = 1`, `1! = 1`. Lanza `ValueError` si `n < 0` y `TypeError` si `n` no es entero.

**Pruebas diseñadas (5):**

| Caso | Entrada | Esperado | Técnica |
|------|---------|----------|---------|
| Caso base | `factorial(0)` | `1` | Definición 0! |
| Caso base | `factorial(1)` | `1` | Definición 1! |
| Caso típico | `factorial(5)` | `120` | 5! |
| Caso mayor | `factorial(7)` | `5040` | 7! |
| Negativo | `factorial(-3)` | `ValueError` | Validación de error |

---

### 5.8 Ejercicio 08 — Número Mayor de una Lista

**Archivos:** `src/ejercicio_08.py`, `src/tests/test_ejercicio_08.py`

**Función:** `obtener_mayor(lista_numeros)`  
Devuelve el valor más alto de la secuencia **sin usar `max()`**. Valida que el argumento sea una `lista`, que no esté vacía y que todos los elementos sean numéricos (`int` o `float`). Lanza `ValueError` (lista vacía) o `TypeError` (no lista / elemento corrupto).

**Pruebas diseñadas (5):**

| Caso | Entrada | Esperado | Técnica |
|------|---------|----------|---------|
| Enteros positivos desordenados | `[4, 12, 8, 3]` | `12` | Lista típica |
| Números negativos | `[-15, -3, -8, -20]` | `-3` | Mayor entre negativos |
| Un elemento | `[42]` | `42` | Lista unielemento |
| Lista vacía | `[]` | `ValueError` | Error lista vacía |
| Elemento corrupto | `[1, 2, "tres"]` | `TypeError` | Elemento no numérico |

---

### 5.9 Ejercicio 09 — Verificación de Palíndromos

**Archivos:** `src/ejercicio_09.py`, `src/tests/test_ejercicio_09.py`

**Función:** `es_palindromo(cadena)`  
Determina si una palabra o frase se lee igual hacia adelante que hacia atrás, ignorando mayúsculas/minúsculas y espacios. Retorna `False` si el texto está vacío o contiene solo espacios. Lanza `TypeError` si el tipo no es `str`.

**Pruebas diseñadas (5):**

| Caso | Entrada | Esperado | Técnica |
|------|---------|----------|---------|
| Palabra palíndroma | `"radar"` | `True` | Caso simple |
| Frase con espacios y mayúsculas | `"Anita lava la tina"` | `True` | Limpieza de texto |
| No palíndroma | `"software"` | `False` | Caso negativo |
| Solo espacios | `" "` | `False` | Cadena vacía/espacios |
| Tipo numérico | `1001` | `TypeError` | Rechazo de tipo |

---

### 5.10 Ejercicio 10 — Clasificación de Calificaciones SENA

**Archivos:** `src/ejercicio_10.py`, `src/tests/test_ejercicio_10.py`

**Función:** `clasificar_nota(nota)`  
Devuelve la descripción cualitativa sobre escala 0.0 a 5.0:
* `4.5 <= nota <= 5.0` → `"Excelente"`
* `3.5 <= nota < 4.5` → `"Bueno"`
* `3.0 <= nota < 3.5` → `"Aceptable"`
* `0.0 <= nota < 3.0` → `"Deficiente"`
* Fuera de escala → `ValueError`
* No numérico → `TypeError`

**Pruebas diseñadas (9, partición de equivalencia y bordes):**

| Caso | Entrada | Esperado | Técnica |
|------|---------|----------|---------|
| Límite superior máximo | `clasificar_nota(5.0)` | `"Excelente"` | Borde superior |
| Borde inferior "Excelente" | `clasificar_nota(4.5)` | `"Excelente"` | Partición Excelente |
| Borde superior "Bueno" | `clasificar_nota(4.4)` | `"Bueno"` | Partición Bueno |
| Borde inferior aprobación mínima | `clasificar_nota(3.0)` | `"Aceptable"` | Partición Aceptable |
| Inmediatamente reprobatorio | `clasificar_nota(2.9)` | `"Deficiente"` | Partición Deficiente |
| Límite inferior absoluto | `clasificar_nota(0.0)` | `"Deficiente"` | Borde inferior escala |
| Fuera de escala < 0 | `clasificar_nota(-0.1)` | `ValueError` | Fuera de rango |
| Fuera de escala > 5 | `clasificar_nota(5.1)` | `ValueError` | Fuera de rango |
| No numérico | `clasificar_nota("4.5")` | `TypeError` | Tipo inválido |

---

### 5.11 Ejercicio 11 — División Segura

**Archivos:** `src/ejercicio_11.py`, `src/tests/test_ejercicio_11.py`

**Función:** `division_segura(dividendo, divisor)`  
Efectúa la división y devuelve el resultado como `float`. Lanza explícitamente `ZeroDivisionError("No es posible dividir entre cero")` si el divisor es 0. Lanza `TypeError` si alguno de los argumentos no es numérico.

**Pruebas diseñadas (5):**

| Caso | Entrada | Esperado | Técnica |
|------|---------|----------|---------|
| División exacta | `division_segura(10, 2)` | `5.0` | Caso feliz |
| División periódica | `division_segura(10, 3)` | `3.333...` (aprox) | `pytest.approx` |
| Cero en dividendo | `division_segura(0, 5)` | `0.0` | Caso borde |
| División por cero | `division_segura(8, 0)` | `ZeroDivisionError` | Captura de excepción |
| Operando no numérico | `division_segura("10", 2)` | `TypeError` | Validación de tipo |

---

### 5.12 Ejercicio 12 — Validación de Diccionario de Usuario

**Archivos:** `src/ejercicio_12.py`, `src/tests/test_ejercicio_12.py`

**Función:** `procesar_usuario(datos_usuario)`  
Recibe un diccionario con claves obligatorias:
* `"id"`: entero positivo mayor a 0.
* `"nombre"`: cadena no vacía.
* `"activo"`: booleano.

Si cumple, devuelve una **copia** del diccionario agregando `"estado_registro": "VALIDADO"`. Lanza `TypeError` si no es diccionario y `ValueError` si falta alguna clave o los tipos son erróneos.

**Pruebas diseñadas (5):**

| Caso | Entrada | Esperado | Técnica |
|------|---------|----------|---------|
| Caso exitoso | `{"id":1,"nombre":"Ana Sofia","activo":True}` | dict con `"estado_registro":"VALIDADO"` | Retorna copia validada |
| Clave faltante | `{"id":1,"nombre":"Ana"}` | `ValueError` | Falta `"activo"` |
| `id` cero o negativo | `{"id":0,...}` / `{"id":-5,...}` | `ValueError` | `id` inválido |
| `nombre` vacío o solo espacios | `""` / `"   "` | `ValueError` | Nombre no válido |
| No es diccionario | `[1, "Ana", True]` | `TypeError` | Tipo incorrecto |

---

## 6. Tabla comparativa de aserciones (pytest vs unittest)

Como referencia rápida del taller, esta tabla muestra cómo se escriben las mismas verificaciones en ambos entornos estándar de Python. En este taller se utilizó exclusivamente **pytest** (sintaxis declarativa).

| Intención | Sintaxis pytest | Sintaxis unittest |
|-----------|-----------------|-------------------|
| Igualdad simple | `assert actual == esperado` | `self.assertEqual(a, b)` |
| Igualdad diccionarios | `assert actual == esperado_dict` | `self.assertDictEqual(a, b)` |
| Desigualdad | `assert actual != no_esperado` | `self.assertNotEqual(a, b)` |
| Booleano Verdadero | `assert actual is True` | `self.assertTrue(actual)` |
| Booleano Falso | `assert actual is False` | `self.assertFalse(actual)` |
| Valor Nulo | `assert actual is None` | `self.assertIsNone(actual)` |
| Aproximación decimal | `assert actual == pytest.approx(3.14, rel=1e-3)` | `self.assertAlmostEqual(a, b, places=3)` |
| Orden numérico | `assert a > b` / `assert a <= b` | `self.assertGreater(a, b)` / `self.assertLessEqual(a, b)` |
| Tipo de dato | `assert isinstance(x, int)` | `self.assertIsInstance(x, int)` |
| Elemento en colección | `assert item in lista` | `self.assertIn(item, lista)` |
| Clave en diccionario | `assert "clave" in diccionario` | `self.assertIn("clave", d)` |
| Longitud de secuencia | `assert len(cadena) == 8` | `self.assertEqual(len(x), 8)` |
| Excepción | `with pytest.raises(ValueError): func()` | `with self.assertRaises(ValueError): func()` |
| Excepción con mensaje | `with pytest.raises(ValueError, match="msg"): func()` | `with self.assertRaisesRegex(ValueError, "msg"): func()` |

---

## 7. Solución de problemas comunes

| Problema | Causa probable | Solución |
|----------|----------------|----------|
| `ImportError: cannot import name ... from partially initialized module` | El archivo fuente contenía `from src.ejercicio_XX import ...` (autoinimportación circular). | Se eliminó esa importación de los archivos fuente; solo queda la definición de la función. |
| `ModuleNotFoundError: No module named 'src'` | Se ejecutó pytest desde una carpeta distinta a la raíz o falta `PYTHONPATH`. | Ejecutar siempre desde la raíz: `python -m pytest -v`. |
| `ModuleNotFoundError: No module named 'pytest'` | pytest no instalado en el entorno activo. | `pip install -r requirements.txt` con el entorno virtual activado. |
| Pruebas no recolectadas (`collected 0 items`) | Los archivos de prueba no tienen prefijo `test_` o están fuera de `src/tests/`. | Verificar que se llamen `test_ejercicio_XX.py` y estén en `src/tests/`. |

---

## 8. Entrega del taller

Según la guía, la evidencia se entrega mediante el enlace al repositorio (GitHub, GitLab, Gitea o Azure Repos). El repositorio debe contener:

1. Historia de commits con los avances de la actividad.
2. Estructura de carpetas indicada (src/ y src/tests/).
3. Archivo `requirements.txt`.
4. Archivo `.gitignore` (ignorando `venv/`, `__pycache__/`, `*.pyc`, `.pytest_cache/`, `.DS_Store`).

**Commit realizado:** `cf42e7a` — "feat: completar 12 ejercicios y suites de pruebas unitarias del taller".

---

## 9. Conclusión

Se implementaron los 12 ejercicios solicitados en la guía del taller, cada uno con su respectiva suite de pruebas unitarias siguiendo el patrón **AAA**, aplicando **Análisis de Valores Límite (BVA)**, **Partición de Equivalencia (EP)** y **Manejo de Excepciones**. El resultado final es **65 pruebas pasando**, lo que confirma que las funciones cumplen con los requisitos y reglas de negocio definidos en el documento original.

> Si requiere ajustes en alguna implementación o prueba, avíseme y los corregimos juntos.