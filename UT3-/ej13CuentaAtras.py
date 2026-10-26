#funcion recursiva que cuenta hacia atras desde un numero dado hasta 0
def cuenta_atras(n):
    if n < 0:
        raise ValueError("El numero debe ser positivo")
    if n == 0:
        print("Fin")
    else:
        print(n)
        cuenta_atras(n-1)

cuenta_atras(5)