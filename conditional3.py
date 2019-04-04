""" Learning about conditionals
    Pay attention to the COLON after the condition
    Note else is different from elif
    """

import random
import sys


def guessing():
    count = 0
    draw = random.randint(0, 100)
    while True:
        guess = int(input('Enter a number between 0 and 100: '))
        count += 1
        if guess > draw:
            print('your guess is higher than the value')
        elif guess == draw:
            print('Congratulations, you got it')
            print('It took you {} tries'.format(count))
            sys.exit()
        else:
            print('your guess is lower than the value')


if __name__ == '__main__':
    guessing()
