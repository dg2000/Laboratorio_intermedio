import numpy as np
import matplotlib as plt


datos = np.loadtxt('camisa.txt')
intentos = np.range(1, len(datos))


plt.plot(intentos, datos)
