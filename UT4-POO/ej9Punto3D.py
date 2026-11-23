#uso de herencia
class Punto():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def distancia(self, otroPunto):
        dx = self.x - otroPunto.x
        dy = self.y - otroPunto.y
        return (dx**2 + dy**2)**0.5

class Punto3D(Punto):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, z):
        self._z = z

    def __str__(self):
        return super().__str__()+": "+str(self.z)

    def distancia(self, otroPunto3D):
        dx = self.x - otroPunto3D.x
        dy = self.y - otroPunto3D.y
        dz = self.z - otroPunto3D.z
        return (dx*dx + dy*dy + dz*dz)**0.5