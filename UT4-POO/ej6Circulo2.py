#vamos a usar encapsulacion convirtiendo metodos en atributos
class Circulo2():
    def __init__(self, radio):
        self.radio = radio #es como el setter pero directamente

    """"Voy a convertir un metodo en un atributo
    usamos el decorador @property para acceder al metodo como atributo"""
    @property
    def radio(self):
        return self._radio
    #usamos @radio.setter para asignar el valor
    @radio.setter
    def radio(self, radio):
        if radio >= 0:
            self._radio = radio
        else:
            raise ValueError("El radio debe ser positivo")
            self._radio = 0
    @radio.deleter
    def radio(self):
        del self._radio


c1 = Circulo2(5)
#accedemos al atributo pero en realidad a traves del metodo
print(c1.radio)
c1.radio = 8
del c1.radio
print(c1.radio)