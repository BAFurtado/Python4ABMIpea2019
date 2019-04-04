import random


def birthdays(n):
    births = list()
    for i in range(n):
        births.append(random.randint(1, 365))
    return births


def has_duplicates(l1):
    l2 = list()
    for i in l1:
        if i not in l2:
            l2.append(i)
        else:
            return True
    return False


def prob(n, r):
    count = 0
    for i in range(r):
        b = birthdays(n)
        if has_duplicates(b) is True:
            count += 1
    print('The probability that at least one student has birthdays \n'
          'on the same day, considering a class of {} students is: {:.2f}%'
          .format(n, count/r * 100))


if __name__ == '__main__':
    # r é o número de iterações
    r = 10000
    n = 41
    # b = birthdays(n)
    # print(b)
    # print(has_duplicates([2, 3, 4]))
    # print(has_duplicates([2, 3, 3]))
    prob(n, r)
