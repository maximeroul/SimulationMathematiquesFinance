# https://stackoverrun.com/fr/q/12363975

import numpy as np
from matplotlib import pyplot as plt
"""
S0 = 100  # initial stock price
K = 100  # strike price
r = 0.05  # risk-free interest rate
sigma = 0.50  # volatility in market
T = 1  # time in years
N = 100  # number of steps within each simulation
deltat = T / N  # time step
i = 100  # number of simulations
discount_factor = np.exp(-r * T)  # discount factor

S = np.zeros([i, N])
t = range(0, N, 1)

for y in range(0, i - 1):
    S[y, 0] = S0
    for x in range(0, N - 1):
        S[y, x + 1] = S[y, x] * (np.exp((r - (sigma ** 2) / 2) * deltat + sigma * deltat * np.random.normal(0, 1)))
    plt.plot(t, S[y])

plt.title('Simulations d un mouvement brownien')
plt.xlabel('Steps')
plt.ylabel('Stock Price')
plt.show()

C = np.zeros((i - 1, 1), dtype=np.float16)
for y in range(0, i - 1):
    C[y] = np.maximum(S[y, N - 1] - K, 0)

CallPayoffAverage = np.average(C)
CallPayoff = discount_factor * CallPayoffAverage
print(CallPayoff)
"""

def rolldice():
    roll = random.randint(1, 100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll >= 50:
        return True


def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager
    wx = []
    vy = []
    currentWager = 1
    while currentWager <= wager_count:
        if rolldice():
            value += wager
            wx.append(currentWager)
            vy.append(value)
        else:
            value -= wager
            wx.append(currentWager)
            vy.append(value)
        currentWager += 1
    plt.plot(wx, vy)


x = 0

while x < 100:
    simple_bettor(100, 1, 1000)
    x += 1

plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()
