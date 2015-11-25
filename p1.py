from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

'''
Script con que se busca estimar la constante de Hubble con los datos
originales de Hubble, y usando un intervalo de confianza del 95%
'''


def metodo_1(x, H):
    return x * H


def metodo_2(v, H):
    return v / H


def bootstrap(datos):
    '''
    bootstrap con intervalo de  confianza  de 95%
    '''
    N = datos.shape[0]
    N_boot = 10000
    H = np.zeros(N_boot)
    for j in range(N_boot):
        aux = np.random.randint(low=0, high=N, size=N)
        datos_falsos = datos[aux][aux]
        x = datos_falsos[:, 0]
        v = datos_falsos[:, 1]
        H_1, cov_1 = curve_fit(metodo_1, x, v, 2)
        H_2, cov_2 = curve_fit(metodo_2, v, x, 2)
        H[j] = (H_1 + H_2) / 2
    H = np.sort(H)
    inf = H[int(N_boot * 0.025)]
    sup = H[int(N_boot * 0.975)]
    print("El intervalo de confianza al 95% ")
    print(inf)
    print(sup)

datos = np.loadtxt("data/hubble_original.dat")
x = datos[:, 0]
v = datos[:, 1]

H_1, cov_1 = curve_fit(metodo_1, x, v, 2)
H_2, cov_2 = curve_fit(metodo_2, v, x, 2)


bisectriz = (H_1 + H_2) / 2
print(bisectriz)


l = np.linspace(-0.2, 2.2, 10**6)
fig = plt.figure()
plt.plot(x, v, 'r*', label=" Datos originales ")
plt.plot(l, metodo_1(l, H_1), 'g', label='H * D')
plt.plot(l, metodo_1(l, H_2), 'b', label='H / v')
plt.plot(l, metodo_1(l, bisectriz), 'r', label='bisectriz')
plt.xlabel("Distancia [Mpc]")
plt.ylabel("Velocidad [Km / s]")
plt.legend(loc=4)
plt.show()

intervalo_confianza = bootstrap(datos)
