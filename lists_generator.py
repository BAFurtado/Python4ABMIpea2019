import random


def generate():

    l = list()
    for i in range(10):
        l.append(random.randint(0, 10))

    return l


if __name__ == '__main__':

    a = generate()
    print(a)

    print(a.pop())
    print(a.pop())

    print(a)

    for i in range(len(a)):
        print(a[i])
