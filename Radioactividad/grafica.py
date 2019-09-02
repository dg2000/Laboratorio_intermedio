import numpy as np
import matplotlib.pyplot as plt



datos = np.loadtxt('camisa.txt')
datos = datos - 3.0
intentos = range(1, len(datos) + 1)

plt.hist(datos, bins=45)
plt.title('Distribucion de conteos con camisa incandescente')
plt.xlabel('Intervalos de conteo')
plt.ylabel('Numero de mediciones')
plt.savefig('camisa.pdf')

prom = np.mean(datos)
dev = np.sqrt(prom)

i = np.where( datos <= (prom+dev) )[0] 
j = np.where( datos >= (prom-dev) )[0]
ij = np.intersect1d(i, j)

porc1 =  ( float(len(ij))/float(len(datos))) * 100.0

a = np.where( datos <= (prom+2.0*dev) )[0]
b = np.where( datos >= (prom-2.0*dev) )[0]
ab = np.intersect1d(a, b)

porc2 = ( ( float(len(ab)) )/( float(len(datos)) ) )*100.0



print 'Para la camisa, el promedio es: ' + str(np.mean(datos)) + ', y la desviacion es: ' + str(dev) 

print 'El porcentaje de datos dentro de C +- sigma es: ' + str(porc1)

print 'El porcentaje de datos dentro de C +- 2sigma es: ' + str(porc2)


