""" Função para converter minutos em horas e minutos
    Exemplifica floor division and modulus
    """


def hour_converter(minutes):
    h = minutes // 60
    m = minutes % 20
    print('{} horas e {} minutos'.format(h, m))


if __name__ == '__main__':
    min = 200
    hour_converter(min)
