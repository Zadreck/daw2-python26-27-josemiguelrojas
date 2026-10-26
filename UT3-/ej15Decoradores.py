#un decorador es una funcion que recibe una funcion por parametro
#la modifica y la devuelve

def tablas(funcion):
    #funcion envoltura
    #1 imprime una cabecera
    #2 ejecuta la funcion
    #3 imprime linea de cierre
    def envoltura(tabla=1):
        print("tabla del %i"%tabla)
        print('-'*15)
        for numero in range(0,11):
            funcion(numero, tabla)
            print('-' * 15)
    return envoltura

#las decoradores se escriben con @
# se crea la funcion suma, se pasa como argumento a tablas
# tablas devuelve envolturas
@tablas
def suma(numero, tabla=1):
    #el %2i indica el ancho
    print('%2i + %2i = %3i' %(tabla, numero ,tabla+numero))

suma(4)

@tablas
def multiplicar(numero, tabla =1):
    print('%2i * %2i = %3i' %(tabla, numero ,tabla*numero))

multiplicar(7)