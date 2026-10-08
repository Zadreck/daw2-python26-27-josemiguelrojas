try:
    numero1 = int (input("Introduce un numero: "))
    numero2 = int (input("Introduce otro numero: "))
    resultado = numero1 / numero2
    print(f"El resultado es:, {resultado}")
except ValueError:
    print("Error debe ser un numero")
    #Mostrar informacion del error:
    print(type(error))
    print(error.args)
    print(error)
except ZeroDivisionError:
    print("debe ser un numero diferente a 0")
except Exception as e: #captura caulquier excepcion no especificada
    print(f"Ocurrio un error inesperado {e}")
else: #el bloque else de un try se ejecuta si no se produce ninguna excepcion
    print("Programa terminado sin errores")
finally: #se ejecuta indistintamente si va bien o mal
    print("Texto que va en el finally")