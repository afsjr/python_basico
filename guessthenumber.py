import random

i = num1 = 0
num2 = random.randrange(1, 100)
try:
    while num1 != num2:
        num1 = int(input('CHOOSE A NUMBER 1 - 100: '))
        i += 1
        if num1 > num2:
            print('Not yet, the secret numer is LOWER ', num1)
        elif num1 < num2:
            print('Not yet, the secret numer is BIGGER ', num1)
        else:
            print('CONGRATS YOU GOT AFTER ', i, 'TRIES')

except Exception as ValueError:
    print('Sorry but you MUST put a integer number, try again ! ')
