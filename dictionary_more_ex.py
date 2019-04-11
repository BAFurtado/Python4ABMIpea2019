
db = dict()
db['025'] = {'nome': 'Sissi', 'cargo': 'mestranda', 'órgão': 'CADE'}
db[155] = {'nome': 'Marlene', 'cargo': 'mestranda', 'órgão': 'BB'}
db[602] = {'nome': 'Gerson', 'cargo': 'mestrando', 'admissão': 2009}
db[231] = {'nome': 'Esa Pekka', 'admissão': 2014, 'num_dep_IR': 4}
db['045'] = {'nome': 'Rafael', 'cargo': 'assistente de pesquisa', 'órgão': 'CADE'}
db[602]['salário'] = 10000
db[602]['salário'] *= 1.15

for k in db.keys():
    print(db[k]['nome'])
    try:
        print(db[k]['órgão'])
    except KeyError:
        print('sem info...')