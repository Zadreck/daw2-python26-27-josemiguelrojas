class Telefono:
    def __init__(self, numero):
        self.__numero = numero  

    def telefonear(self):
        print(f"Llamando desde el número {self.__numero}...")

    def colgar(self):
        print("Llamada finalizada.")

    def __str__(self):
        return f"Teléfono: {self.__numero}"


class Camara:
    def __init__(self, mpx):
        self.__mpx = mpx  

    def fotografiar(self):
        print(f"Tomando foto con resolución de {self.__mpx} megapíxeles.")

    def __str__(self):
        return f"Cámara: {self.__mpx} Mpx"


class Reproductor:
    def __init__(self, capacidad):
        self.__capacidad = capacidad  

    def reproducirmp3(self):
        print("Reproduciendo archivo MP3...")

    def reproducirvideo(self):
        print("Reproduciendo vídeo...")

    def __str__(self):
        return f"Reproductor: {self.__capacidad} GB"


class Movil(Telefono, Camara, Reproductor):
    def __init__(self, numero, mpx, capacidad):
        Telefono.__init__(self, numero)
        Camara.__init__(self, mpx)
        Reproductor.__init__(self, capacidad)

    def __str__(self):
        return (
            f"Móvil -> {Telefono.__str__(self)} | "
            f"{Camara.__str__(self)} | "
            f"{Reproductor.__str__(self)}"
        )