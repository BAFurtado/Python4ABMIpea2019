""" Learning about conditionals
    Pay attention to the COLON after the condition
    Note else is different from elif
    """

import random


def t_valor(x, draw, c):
    if x > draw:
        print('your guess is higher than the value')
    elif x == draw:
        print('Congratulations, you got it')
        print('It took you {} tries'.format(c))
        quit()
    else:
        print('your guess is lower than the value')


if __name__ == '__main__':
    count = 0
    value = random.randint(0, 100)
    while True:
        guess = int(input('Enter a number between 0 and 100: '))
        count += 1
        t_valor(guess, value, count)
