import pandas as pd


class T:
    def __init__(self, a, b):
        self.col_a = a
        self.col_b = b


def minimum_a(l_objs):
    # Retorna objeto com valor col_a mínimo
    minimum = min(i.col_b for i in listats)
    for i in l_objs:
        if i.col_b == minimum:
            return i


if __name__ == '__main__':
    data = pd.read_csv('nome_do_arquivo.csv', sep=';')
    listats = []
    for i in range(len(data)):
        listats.append(T(data.loc[i, 'col_a'], data.loc[i, 'col_b']))
    print(minimum_a(listats))
