""" Essa é uma função que calcula o volume de um
    cubo
"""


def volume(a, b, c):
    return a * b * c


if __name__ == '__main__':
    h = 3.14
    b = 3.14
    p = 3.14854
    print('O resultado é {:.2f}'.format(volume(h, b, p)))