import math


def area(radio):
    """Calculo el area de un circulo dado el radio"""
    if radio < 0:
        raise ValueError("El radio no puede ser negativo")
    return math.pi * radio **2

print(area(2))