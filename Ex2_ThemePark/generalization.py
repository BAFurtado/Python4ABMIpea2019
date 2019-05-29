from Ex2_ThemePark import interactions
from Ex2_ThemePark import parameters
import os


def main(p):
    a = list()
    for i in range(1, p['num_simulations'] + 1):
        a.append((p['increment_num_visitors_by'] * i ** p['increment_exponencial']))
    s = [p['num_shops']] * len(a)
    file = 'accounts_results.csv'
    if os.path.exists(file):
        os.remove(file)
    with open(file, 'a') as f:
        f.write('num_consumers;num_shops;avg_fun;avg_shop_balance;avg_consumer_balance\n')
        for i in range(len(a)):
            res = interactions.main(a[i], s[i], p)
            f.write('{};{};{:.2f};{:.2f};{:.2f}\n'.format(a[i], s[i], res[0], res[1], res[2]))


if __name__ == '__main__':
    # Número de repetições 'm'
    # m = {'num_simulations': 10}
    params = parameters.params
    main(params)
