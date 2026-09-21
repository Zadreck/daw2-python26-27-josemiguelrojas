#Pedir num por pantalla
from itsdangerous.encoding import int_to_bytes

num1 = input ("Dame el numero 1:")
num2 = input ("Dame el numero 2:")
print(num1+num2)
print(int(num1)+int(num2))
#pasar a binario
num3 =input("Num a convertir: ")
print(bin(int(num3)))