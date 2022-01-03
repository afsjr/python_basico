import random

def dice1():
    print('rolling the first dice : ')
    lado1 = random.randrange(1,6,1)
    print('rolling the second dice : ')
    lado2 = random.randrange(1, 6, 1)
    return lado1, lado2

try:
    # lets play the dices
    lado1,lado2 = dice1()
    print('The sum between dice(1) -> ', lado1,'and the dice(2)-> ', lado2, '= ', lado1+lado2)
except:
    pass

