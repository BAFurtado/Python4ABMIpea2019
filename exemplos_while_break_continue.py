

def got_it(number):
    while number > 0:
        print('Got it!')
        number -= 1


def while_true():
    while True:
        ipt = input('Do you wanna stop?')
        if ipt == 'YES!':
            break


def for_only_odd(n):
    for i in range(n):
        n -= 1
        if n % 2 == 0:
            print(n)

        else:
            continue
            print('This is an never going to print')


if __name__ == '__main__':
    got_it(10)
    # while_true()
    for_only_odd(10)
