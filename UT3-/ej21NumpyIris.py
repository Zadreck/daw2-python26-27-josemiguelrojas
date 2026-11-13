import numpy as np
#leemos el archivo csv con los datos
#lo cargams en una matriz y quto la primera fila
iris = np.loadtxt('./iris.csv', skiprows=1, delimiter=',')
print("Matriz de datos de iris \n", iris.shape)
#5 primeras filas
print("5 primeras filas: ", iris[:5,: ])
#medias de esas filas
print("5 primeras filas:\n", np.mean(iris[:5,: ]))
#media por columna
print("Media por columna:\n", np.mean(iris, axis=0))
#dime de cada caracteristica el valor minimo (min)
print("Valor minimo por columna:\n", np.min(iris, axis=0))
#dime las filas que tienen un largo del petalo mayor a 5.0
print("Filas con largo del petalo mayor a 5.0:\n", iris[iris[:, 2] > 5.0])
#de las filas 50 a 99, muestra solo largo y ancho del petalo
print("Largo y ancho del petalo en las filas 50 a 99:\n", iris[50:100, 2:4])
#normalizar para ver los valores en el rango
#se hace dividiendo el valor a normalizar - el valor minimo dividio por la diferencia
#entre max y min

print("", (iris - iris.min(axis=0)) / (iris.max(axis=0) - iris.min(axis=0)) )