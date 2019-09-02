import numpy as np
import matplotlib.pyplot as plt 

r = np.loadtxt('distancia.txt')[:,0]
total = np.loadtxt('distancia.txt')[:,1]
ter = rer = np.loadtxt('distancia.txt')[:,2]
alfa = total - np.loadtxt('distancia.txt')[:,3]
rer = np.loadtxt('distancia.txt')[:,7]
aer = 4.0*np.loadtxt('distancia.txt')[:,2] + np.loadtxt('distancia.txt')[:,4]
beta = np.loadtxt('distancia.txt')[:,3] - np.loadtxt('distancia.txt')[:,5]
ber = np.loadtxt('distancia.txt')[:,4] + np.loadtxt('distancia.txt')[:,6]
gamma = np.loadtxt('distancia.txt')[:,5]
ger = np.loadtxt('distancia.txt')[:,6]


a = 1/r
a = a*a


plt.errorbar(r, total, xerr=rer, yerr=ter, color ='yellow', label='Total')
plt.errorbar(r, alfa,xerr=rer, yerr=aer, color='blue', label='Alfa')
plt.errorbar(r, beta,xerr=rer, yerr=ber, color='green', label ='Beta')
plt.errorbar(r, gamma, xerr=rer, yerr=ger, color='red', label ='Gamma')


plt.title('Decaimiento con la distancia')
plt.xlabel('Distancia (cm)')
plt.ylabel('Conteos')
plt.legend(loc=0)

plt.savefig('distancia.pdf')

plt.figure()
plt.errorbar(a, gamma*100.0, xerr=4.0*rer*rer, yerr=100.0*ger, label='Gamma corregido')
plt.xlabel('Distancia (1/cm-2)')
plt.ylabel('Conteos')
plt.title('Decaimiento gamma vs 1/r2')
plt.legend(loc=0)
plt.savefig('gamma.pdf')


