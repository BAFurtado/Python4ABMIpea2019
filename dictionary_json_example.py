""" Class example to create and maintain a persistent database using JSON and dictionaries
    Para usar é necessário sempre entrar com o valor em formato DICIONÁRIO
"""


import json
import os
from collections import defaultdict


def my_database(k, v):
    # Checking if database exists
    ''' args:
        return '''
    if os.path.exists('my_database.json'):
        with open('my_database.json', 'r') as f:
            data = json.load(f)
    # If not saved before, create dictionary for the first time
    else:
        # Prepara o dicionário para receber outros dicionários como valores
        data = defaultdict(dict)

    # Adding data to the dictionary
    # Teste para quando a key é introduzida pela primeira vez
    if k not in data:
        data[k] = v
    # Caso a key já exista no dicionário. Mètodo update recebe um dicionário
    else:
        data[k].update(v)

    # Saving it in file
    with open('my_database.json', 'w') as f:
        json.dump(data, f)

    print('Current dictionary is: \n{}'.format(data))
    return data


if __name__ == '__main__':
    # key = '054'
    # value = {'admission': '04/01/2019'}
    # d = my_database(key, value)
    key = '021'
    value = {'nome': 'Paul', 'órgão': 'ABIN'}
    d = my_database(key, value)
