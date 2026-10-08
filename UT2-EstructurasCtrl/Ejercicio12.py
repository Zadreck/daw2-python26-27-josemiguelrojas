numero = int(input("Introduce un número entero: "))

if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    factorial = 1
    i = 2
    while i <= numero:
        factorial *= i
        i += 1
    print(f"El factorial de {numero} es {factorial}")