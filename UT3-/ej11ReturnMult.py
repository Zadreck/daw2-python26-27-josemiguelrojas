#en python una funcion puede devolver varios valores
def operar(n1,n2):
    return n1+n2, n1-n2, n1*n2

suma, resta , producto = operar(12,5)
print(suma)
print(resta)
print(producto)