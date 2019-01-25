""" Building a simple dictioanry """

from collections import defaultdict

my_dict = defaultdict(list)

NAMES = ['Maria', 'Priscila', 'Teo', 'Nina', 'Júnior', 'Paulo', 'Rita', 'Rui', 'Pamela']
AGES = [30, 29, None, 45, 31, 28, 25, 41, 15]
BIRTHDAYS = ['10-01', '13-09', '10-11', '20-01', '23-08', '31-01', '15-06', '02-08', '03-07']
AFFILIATION = ['MPU', 'TCU', 'MJ', 'ME', 'MT', 'PRESI', 'INEP', 'INPE', 'BC']

for i in range(len(NAMES)):
    for detail in [AGES, BIRTHDAYS, AFFILIATION]:
        my_dict[NAMES[i]].append(detail[i])

for key in my_dict.keys():
    print(key, my_dict[key])
