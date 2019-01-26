""" Learning about conditionals
    Pay attention to the COLON after the condition
    Note else is different from elif
    """


def determine_input(x):
    if type(x) == str:
        print('you entered a string')
        t_str(x)
    else:
        print('you probably entered a number')
        t_valor(x)


def t_valor(x):
    if x > 0:
        print('x is positive')
    elif x == 0:
        print('x is zero')
    else:
        print('x is negative')


def t_str(x):
    if x in 'aeiou':
        print('x is a vowel')
    elif x == 'z':
        print('x is z')
    elif x in 'AEIOU':
        print('x is a capital vowel')
    else:
        print("I don't know what you entered")


if __name__ == '__main__':
    y = 20
    determine_input(y)
    y = 'aio'
    determine_input(y)
