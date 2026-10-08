def validar_edad(edad):
    if not isinstance(edad, int):
        print("debe ser un numero")
        raise TypeError("La edad debe ser un numero natural")
    #validamos que la edad este entre 1 y 100
    if not 1 < edad < 100:
        raise ValueError ("La edad debe estar entre 1 y 100")
    return edad

try:
    mi_edad = "21"
    mi_edad_validada = validar_edad(mi_edad)
except (TypeError, ValueError) as e:
    print(f"Error al validar la edad: {e}")
