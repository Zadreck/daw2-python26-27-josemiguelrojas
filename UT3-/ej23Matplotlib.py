import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#datos a visualizar
t = np.arange(0.0, 2.0, 0.01)
s = 1+np.sin(2*np.pi*t) #coordenada y
plt.plot(t,s)
#etiqueta en el eje x
plt.xlabel('tiempo(s)')
#etiqueta en el eje y
plt.ylabel('voltaje /mv')
plt.grid(True)
plt.savefig('plt1.png')
plt.show()