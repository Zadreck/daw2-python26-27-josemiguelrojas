#biblioteca de computacion cientifica
#estadistica y analisis de grandes volumenes de datos
#intengra con Pandas, Matplotlib, SciPy Sckit-learn
import numpy as np
print("Version; ", np.__version__)

#usamos la estructura optimizada para numeros->array
a = np.array([1,2,3,4,5])
print("Array de numpy", a)
print("Array de ceros,", np.zeros(5))
#genera un array de 2 filas y 3 columnas
print(np.ones((2,3)))
#genere un array de 0 a 10 contando de 2 en 2
print("array 0-10", np.arange(0,10,2))
print("array numeros aleatorios 2 columnas")
print(np.random.rand(3,2))

mat1 = np.array([[1,2], [3,4]])
print(mat1)
mat2 = np.ones((2,2))
print("Matriz de unos 2x2\n", mat2)
print("dimensiones mat2", mat2.shape)
#operaciones con matrices
matSuma = mat1 + mat2
print("suma=\n",matSuma)

matProd = mat1 * mat2
print("prod=\n",matSuma)

#inversa de una matriz
#es una matriz tal que al multipiplicar de una matriz
print("dada una matriz:\n", mat1)
print("la inversa de la matriz: ",np.linalg.inv(mat1))

#generar una matriz con valores del 1 al 10
mat = np.arange(1, 10).reshape((3,3))
print("mat=", mat)
#acceder a una celda
print("fila2, columna2 es: " ,mat[1,1])
#acceder a una fila
print("fila 2 es: ",mat[1,:])
#acceder a una columna
print("col 3 es: \n", mat[:, 2:3])
#aplicar filtros
print("Los mayores de 5 son:",mat[mat>5])
#la media aplicada a matrices
print("", np.mean(mat))
#media de las filas
print("media filas: ", np.mean(mat, axis=1))
#media de las columnas
print("media columnas: ", np.mean(mat, axis=0))