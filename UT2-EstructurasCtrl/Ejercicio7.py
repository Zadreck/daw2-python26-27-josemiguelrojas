def validar_edad(edad):
    if not isinstance(edad, int):
        print("debe sr un numero")
        raise TypeError("La edad debe ser un numero natural")
    return edad

try:
    mi_edad = validar_edad("21asdf")
    mi_edad_validada = validar_edad(mi_edad)
except TypeError as e:
    print(f"Error al validar la edad: {e}")
