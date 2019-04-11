""" Files examples
"""


def first():
    with open('experience.txt', 'w') as f:
        f.write('This is my first saved output\n')


def second():
    with open('experience.txt', 'a') as f:
        f.write('This is my second saved output\n')


# Let's try with some numbers:
def numbers():
    l = list()
    for i in range(10):
        l.append(i ** i)

    with open('experience.txt', 'a') as f:
        for each in l:
            f.write('{};'.format(str(each)))


# What have we done?
def reading():
    with open('experience.txt', 'r') as f:
        lida = f.read()
    # print(lida)
    return lida


def recover_list(li):
    li = li.split('\n')

    recovered = list()
    for each in li[2].split(';'):
        if len(each) > 0:
            recovered.append(int(each))

    # print(recovered)
    return recovered


def sum_list(recovered):
    print('A soma da lista recuperada é {:,.0f}'.format(sum(recovered)))


if __name__ == '__main__':
    # first()
    # second()
    # numbers()
    r = reading()
    ll = recover_list(r)
    sum_list(ll)
