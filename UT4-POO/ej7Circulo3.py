class Circulo3():
    def __init__(self, radio):
        self.radio = radio

#get
    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, radio):
            if radio >= 0:
                self._radio = radio
            else:
                raise ValueError("El radio debe ser positivo")
                self._radio = 0
#deleter               
    @radio.deleter
    def radio(self):
        del self._radio

    #definimos o adaptamos metodos
    def __str__(self):
        clase = type(self).__name__
        msg = "{0} de radio {1}"
        return msg.format(clase, self.radio)
    #ahora con repr que se usa en desarrollo y depuracion
    def __repr__(self):
        clase = type(self).__name__
        msg = "{0} ({1})"
        return msg.format(clase, self.radio)

    #tengo que definir el metodo para comparar objetos de la clase circulo
    def __eq__(self, otroObjetoQueTenga):  
        return self.radio == otroObjetoQueTenga.radio
    def __add__(self, otroParaSumar):
        return self.radio + otroParaSumar.radio
    
circ1 = Circulo3(34)
print(circ1)
print(repr(circ1))
circ2 = Circulo3(34)
print(circ1==circ2)