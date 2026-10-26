def factorial (n):
    #calculamos el factorial de un numero
    resultado = 1;
    for i in range (1,n+1):
        resultado*=i
    return resultado

print("Resultado del factorial de 6: ",factorial(6))