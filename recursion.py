def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        return countdown(n-1)


if __name__ == '__main__':
    m = 1000
    countdown(m)
