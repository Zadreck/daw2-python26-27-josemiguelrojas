import math
class Punto:
    """Representacion de un punto en el plano x,y"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distancia(self, otroPuntoQueMeDigan):
        dx =self.x - otroPuntoQueMeDigan.x
        dy =self.y - otroPuntoQueMeDigan.y
        return math.sqrt((dx*dx + dy*dy))

# Declaro variables objeto que sean del tipo Punto.
punto1 = Punto()
print(punto1.x, punto1.y)
punto2 = Punto(18, 29)
print(punto2.x, punto2.y)
print(punto1.distancia((punto2)))