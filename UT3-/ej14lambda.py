#funciones lambda, finciones que se definene en una linea
#la forma clasica:
from ej13CuentaAtras import cuenta_atras


def cuadrado_orig(x):
    return x**2

cuadrado = lambda x: x**2
print(cuadrado(2))

print((lambda x: x**2) (3))

print((lambda nombre: "hola " + nombre) ("Federico"))

pares = [(1,"uno"), (2,"dos"), (3,"tres"), (4,"cuatro"), (5,"cinco")]
#ordena por el calor de key
#y pair [1] devuelve el segundo valor elemento (el texto)
pares.sort(key=lambda pair :pair[1])
print(pares)