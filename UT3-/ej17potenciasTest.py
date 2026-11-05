#vamos a utilizar las funciones definidas en ej17
#namespace
import ej17potencias
#usamos la funcion dir para ver los metodos
print(dir(ej17potencias))
print(ej17potencias.cuadrado(3))
print(ej17potencias.cubo(4))
#otras formas
import ej17potencias as p
print(p.cuadrado(12))
#importar funciones independientes
from ej17potencias import cuadrado as pcuad
from ej17potencias import cubo as pcub
print(pcuad(5))
print(pcub(4))