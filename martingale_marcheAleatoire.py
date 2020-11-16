import random
from matplotlib import pyplot as plt

'''
Simple bettor, betting the same amount each time.
'''


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

simple_bettor(100, 1, 1000)

plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()
