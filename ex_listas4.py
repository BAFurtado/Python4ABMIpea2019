

def tabuada(num):
    for i in range(1, 11):
        print('{} x {} = {}'.format(num, i, num * i))

if __name__ == '__main__':
    n = 8
    tabuada(n)