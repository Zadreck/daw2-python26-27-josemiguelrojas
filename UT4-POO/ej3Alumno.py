#ejemplo del uso de atributos estaticos (o de clase)
class Alumno():
    contador = 0

    def __init__(self, nombre=" "):
        self.nombre = nombre
        Alumno.contador += 1


alumno0 = Alumno()
print("Nombre del alumno 0:" ,alumno0.nombre)
alumno1 = Alumno("Pepe")
print("Nombre del alumno 1:" ,alumno1.nombre)
alumno2 = Alumno("Federico")
print("Nombre del alumno 2:" ,alumno2.nombre)
alumno3 = Alumno("Gabriela")
print("Nombre del alumno 3:" ,alumno3.nombre)
#cuantos alumnos hay en clase
print("En clase el num de alumnos es:" ,Alumno.contador)