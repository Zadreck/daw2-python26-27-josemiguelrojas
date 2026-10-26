#funcion con parametros por defecto
"""Funcion que tiene 4 parametros
-numero
-otro numero
-operador
respuesta por defecto"""

def operar(n1, n2 , operador='+', respuesta='resultado es: '):
    if operador == "+":
        return  respuesta + str(n1+n2)
    elif operador =="-":
        return  respuesta + str(n1-n2)
    else:
        return "Error, operador no valido"
print(operar(5,7))
print(operar(5,7,"-"))
print(operar(5,7,"-","El resultado de la esta es:"))
print(operar(5,7,"*"))