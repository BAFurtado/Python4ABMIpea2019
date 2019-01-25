""" Exemplo de histogramas usando dicionários.
    Adaptado de Think Python. Chapter 11

"""
import lists_generator


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


if __name__ == '__main__':
    d = histogram('paralelepipedo')
    print(d)
    e = histogram(lists_generator.generate())
    print(e)
