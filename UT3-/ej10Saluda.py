#parametro **kwargs
def saludar(nombre : str ="pepe", **kwargs):
    cadena = nombre
    for valor in kwargs.values():
        cadena=cadena+" "+valor
    return "Hola "+cadena

print(saludar())
print(saludar(nombre="Aneth"))
print(saludar(nombre="pepe", nombre2="juan", nombre3="alicia"))