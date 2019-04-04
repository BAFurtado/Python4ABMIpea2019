""" An equilateral triangle is a triangle in which all three sides are equal.
    A scalene triangle is a triangle that has three unequal sides.
    An isosceles triangle is a triangle with (at least) two equal sides.
"""


def which_triangle(a, b, c):
    # Se todos são iguais
    if a == b == c:
        print('Your triangle is equilateral and isosceles')
    elif a == b or b == c or a == c:
        print('Your triangle is isosceles')
    else:
        print('Your triangle is scalene')


if __name__ == '__main__':
    l1 = 4
    l2 = 5
    l3 = 6

    which_triangle(l1, l2, l3)