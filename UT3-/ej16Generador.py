#resultados paso a paso
#el yield devuelve los valores 1 a 1
def par(inicio, fin):
    for i in range(inicio,fin):
        if i%2 == 0:
            yield i
datos=par(1,50)
print(next(datos))
print(next(datos))
print(next(datos))