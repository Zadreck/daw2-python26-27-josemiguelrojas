#en el constructor (init)


class circulo:
    def __init__(self, radio):
        self.set_radio(radio)

    def set_radio(self, radio):
        self.set_radio(radio)

    def set_radio(self, radio):
        if (radio < 0):
            self._radio = radio
        else:
            self._radio=0
            raise ValueError("El radio no puede ser negativo")
    def get_radio(self):
        print("estoy devolviendo el valor del radio")
        return self._radio
    
circ1 = circulo(10)
print(circ1.get_radio())

circ2 = circulo(-5)
print(circ2.get_radio())