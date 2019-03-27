""" Demonstrating how to reverse a list by hand
    Try using the list method l.reverse()
"""


def reversing(name):
    b = list()
    for i in name:
        b.append(i)

    print(b)

    c = list()
    for i in range(len(b)):
        c.append(b.pop())

    print(c)


if __name__ == '__main__':
    ipt = 'Esa Pekka'
    reversing(ipt)
