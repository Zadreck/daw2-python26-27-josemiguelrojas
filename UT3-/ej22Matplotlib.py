#librerias para visualizar datos
import matplotlib.pyplot as plt
import numpy as np

#ejemplo 1 plots simples
#plots sencillo: eje x de 1-4 y eje y de 1-16
#plt.plot([1,2,3,4], [1,4,9,16])
#varios plots en la misma grafica
#plt.plot([1,2,3,4], [1,4,9,16])
#plt.plot([1,2,3,4], [5,1,2,17])
#plt.show()

#puntps individuales a scatter plots
#plt.scatter([1,2,3,4], [1,4,9,16])
#plt.show()

#con  numpy vector de puntos de 0 a 5 sumando de 0.2 en 0.2
t = np.arange(0.,5,0.2)
#lo dibujo con 3 estilos
#t,t,'r--' eje x va t, en eje y va t, en color rojo y discontinuo
plt.plot(t,t,'r--',t,t**2,'bs', t, t**3, 'g^')
plt.show()
