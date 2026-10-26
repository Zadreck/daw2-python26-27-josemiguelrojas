#funciones con parametros obligatorios y opcionales
# n primer argumento obligatorio y a apartir de ahi argumentos adicionales
def sumar (n, *args):
    resultado = n
    for i in args:
        resultado+=i
    return  resultado

print(sumar(2,3))
print(sumar(3,4,5,6,7))
lista=[1,2,3,4,5,6,7,8]
print(sumar(*lista))