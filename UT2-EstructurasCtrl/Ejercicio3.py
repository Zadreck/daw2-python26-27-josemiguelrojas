print("Contando con for:")
for i in range(1,6):
    print(i, end=" ")
#otra opcion, range(10) genera una secuencia del 0 al 9
print("\nAhora de 10")
for i in range(10):
    if i==3:
        print("hola 3")
    print (i, end=" ")

#iterar con listas
nombres=["Carlos", "Samuel", "Bianca"]
for i in nombres:
    print (i)