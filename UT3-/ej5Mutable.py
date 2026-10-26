#las listas son objetos mutables en Python
#cuando una lista se pasa a una fuuncion, la funcion puede modificar la original

def f(lista):
    lista.append(5)

listaOrig =[1,2]
f(listaOrig)
print(listaOrig)