
def celsius_a_fahrenheit(celsius):
    if type(celsius) not in (int, float):
        raise TypeError("La temperatura debe ser un número")
    if celsius < -273.15:
        raise ValueError("Temperatura por debajo del cero absoluto (-273.15 °C)")
    return (celsius * 1.8) + 32
