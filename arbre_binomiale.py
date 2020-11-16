import random
import matplotlib.pyplot as plt

S0 = 10
u = 1.05
d = 0.95
p = 0.55
iteration = 100
simulation = 50


def simulation_binomiale(depart, u, d, p, iteration):
    param = 1
    liste = [depart]

    for i in range(iteration):
        rand = random.random()

        if rand < p:
            param = u * param
        else:
            param = d * param

        iter = param * S0
        liste.append(iter)

    plt.plot(liste)

    return liste


x = 0

while x < simulation:
    simulation_binomiale(S0, u, d, p, iteration)
    x += 1

plt.ylabel('Prix')
plt.xlabel('Temps')
plt.show()
