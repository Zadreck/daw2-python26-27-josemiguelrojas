class gato():
    def hablar(self):
        print("miau")

class perro():
    def hablar(self):
        print("guau")

#funcin con parametro animal asi con cualquier metodo que tenga un hablar() puede ser pasado como parametro
def escucharMascota(animal):
    animal.hablar()

g = gato()
p = perro()
escucharMascota(g)
escucharMascota(p)