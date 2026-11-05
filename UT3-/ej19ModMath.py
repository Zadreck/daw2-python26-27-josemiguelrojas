import math
from traceback import print_tb

print("Factorial de 5: ", math.factorial(5))
print("2 al cubo: ", math.pow(2,3))
print("Raiz cuadrada de 7: ", math.sqrt(7))
print("coseno de 1: ", math.cos(1))
print("PI", math.pi)
print("logaritmo: ", math.log(10))

print("***modulo fractions***")
from fractions import Fraction
a = Fraction(2,3)
print("Fraction(2,3) ",a)
b = Fraction(1.5)
print("fraction(1.5)",b)
c = a + b
print("suma= ", c)

print("***modulo statistics***")
import statistics
print("media aritmetica de 1,4,5,2,6 es:", statistics.mean([1,4,2,5,6]))
#valor central de la lista ordenada
print("mediana ", statistics.median([1,4,2,5,6]))

print("\n****MODULO RANDOM**")
import random
print("Numero aleatorio entre 5, 50: ",random.randint(5,50))
palabras = ["hola", "k", "ase", "hoy"]
print(random.choice(palabras))
#baraja la lista(reaordenar, desordenar)
random.shuffle(palabras)
print(palabras)

otrasPalabras = random.sample(palabras, 3)
print(otrasPalabras)