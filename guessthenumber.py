import random

i = num2 = num1 = 0
num2 = random.randrange(1, 100)
while True:
    num1 = int(input('digite um número de 1 - 100: '))
    i += 1
    if num1 > num2:
        print('ainda não encontrei, tente um valor menor diferente de', num1)
    elif num1 < num2:
        print('ainda não encontrei, tente um valor maior diferente de', num1)
    else:
        print('parabéns, você acertou depois de', i, 'tentativas')
        False
