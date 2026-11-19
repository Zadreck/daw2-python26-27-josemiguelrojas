#vamos a crear la primera clase
class Clase():
    #atributos de la clase
    at_clase=1
    #definimos un metodo que usa el atributo
    def metodo(self):
        #y este metodo tiene un atributo del objeto (no de la clase)
        self.at.objeto =358948

#crea un objeto de esta clase
objeto = Clase()
#es del tipo
print(type(objeto))
#para ver el valor del atributo de la clase
print(Clase.at_clase)
#acceso al objeto
#llamo al metodo para que cree el valor
objeto.metodo()