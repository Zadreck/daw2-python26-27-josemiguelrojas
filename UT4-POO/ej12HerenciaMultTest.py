from ej11HerenciaMultMovil import Movil, Telefono
miMovil = Movil(666123456, 12,2)
#vemos atributos y métodos
print(dir(miMovil))
print(miMovil )

print("Es instancia?", isinstance(miMovil, Movil))
print("Es hija?", issubclass(Movil, Telefono))