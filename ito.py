from math import sqrt
import random
import matplotlib.pyplot as plt

N = 100
S0 = 10
T = 1
delta_t = T / N
iteration = 100


def ito():
    Liste_Variation = [0]
    Liste_W = [0]

    for i in range(1, N):
        W_dti = sqrt(delta_t) * random.random()
        Liste_W.append(Liste_W[-1] + W_dti)

        Liste_Variation.append(Liste_Variation[-1] + (Liste_W[-1] - Liste_W[-2]) ^ 2)

    plt.plot(Liste_Variation)


for i in range(iteration):
    ito()

plt.show()
