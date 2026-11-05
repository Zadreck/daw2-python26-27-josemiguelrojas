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