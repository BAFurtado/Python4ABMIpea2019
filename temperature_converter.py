""" Função para converter entre Celsius e Fahreneith
"""


def to_celsius(f):
    return (f - 32) / 9 * 5


def to_f(c):
    return (c * 9 / 5) + 32


if __name__ == '__main__':
    c = 10
    print(to_celsius(c))
