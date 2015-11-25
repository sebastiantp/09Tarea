from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def montecarlo(datos1,  datos2, alfa, N):
    '''Recibe un arreglo de datos y retorna un
    intervalo de confianza al 100*(1-alfa)% usando
    una simulacion de montecarlo'''

    flujo1 = datos1[0]
    error1 = datos1[1]
    flujo2 = datos2[0]
    error2 = datos2[1]
    a = np.zeros(N)
    b = np.zeros(N)
    for j in range(N):
        aux = np.random.normal(0, 1, size=len(flujo1))
        muestra1 = flujo1 + error1 * aux
        muestra2 = flujo2 + error2 * aux
        b[i], a[i] = np.polyfit(muestra1, muestra2, 1)
    b = np.sort(b)
    a = np.sort(a)
    liminfa = a[int(N * alfa)]
    limsupa = a[int(N * (1 - alfa))]
    liminfb = b[int(N * alfa)]
    limsupb = b[int(N * (1 - alfa))]
    return liminfa, limsupa, liminfb, limsupb


datos = (3.631 *
         np.loadtxt('data/DR9Q.dat', usecols=(80, 81, 82, 83)))
a = datos[:, 0]
b = datos[:, 1]
c = datos[:, 2]
d = datos[:, 3]
datosI = np.array([a, b])
datosZ = np.array([c, d])
polyfit = np.polyfit(datosI[0], datosZ[0], 1)
y = np.zeros(len(datosI[0]))
k = 0
for i in datosI[0]:
    y[k] = polyfit[0] * i + polyfit[1]
    k += 1
fig3 = plt.figure(3)
fig3.clf()
plt.plot(datosI[0], y, 'b-')
plt.plot(datosI[0], datosZ[0], 'r*')
plt.xlabel('Flujo banda I ($1e-6 \ Jy$)')
plt.ylabel(r'Flujo banda Z ($1e-6 \ Jy$)')
plt.title(r'Grafico flujo banda I vs flujo banda Z')
plt.grid(True)

plt.show()


alfa = 0.05
N = 10000
liminfa, limsupa, liminfb, limsupb = montecarlo(datosI, datosZ, alfa, N)
print('Parametro A = ')
print(polyfit[0])
print('Parametro B = ')
print(polyfit[1])
print('El limite inferior para  A ')
print(str(liminfa))
print('limite suprior')
print(limsupa)
print('El limite inferior para  B ')
print(liminfb)
print('limite suprior')
print(limsupb)
