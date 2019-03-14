""" Script que calcula a área do círculo
    Exemplo de função comentada
    Python for ABM - Ipea - Março 2019
    """

import math


def area_circle(r):
    """ Função que calcula área do círculo.
        Parâmetro: r - o raio do círculo
        Retorna a área
        """

    # Fórmula área
    area = math.pi * r ** 2
    return area


""" Running the module individually.
    Quando importado, o código abaixo não roda
    """
if __name__ == '__main__':
    raio = 2
    result = area_circle(raio)
    # Exemplo de formatação de output com float e duas casas decimais usando format
    print('A área é: {:.2f}'.format(result))
