def factorial(n):
    if n<0:
        raise ValueError("El numero debe ser positivo")
    if n==0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))