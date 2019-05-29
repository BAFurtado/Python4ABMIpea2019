

params = {'capacity': [4, 8],
          'cost': [20, 30],
          'fun': [100, 105],
          'salaries': [20, 30],
          'increment_num_visitors_by': 25,
          'increment_exponencial': 1,
          'num_simulations': 20,
          'num_shops': 20
}

print('Capacidade máxima {}'.format(params['capacity'][1] * params['num_shops']))
print('Máximo clientes {}'.format(params['num_simulations'] *
                                  params['increment_num_visitors_by'] ** params['increment_exponencial']))
