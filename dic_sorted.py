""" Exemplo de sorted histogramas usando dicionários.
    Adaptado de Think Python. Chapter 11

"""
import lists_generator


def histogram(data):
    d = dict()
    for each in data:
        d[each] = d.get(each, 0) + 1
    return d


def print_sorted(d):
    for key in sorted(d):
        print(key, d[key])


if __name__ == '__main__':
    string1 = 'paralelepipedo'
    d1 = histogram(string1)
    print(string1)
    print_sorted(d1)
    print('')
    d2 = histogram(lists_generator.generate())
    print('lista aleatória')
    print_sorted(d2)
