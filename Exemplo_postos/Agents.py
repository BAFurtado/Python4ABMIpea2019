# A Distribuidora seta o preço inicial (randomico)
# Os postos tem que ter volume e preço inicial (inicial é randomico?)
# Consumidores tem que ter quantidade de tanque cheio inicial (fazer na classe)
import random


class Distribuidores:
    def __init__(self):
        self.custo = random.randrange(0, 10)

    def altera_custo(self, param):
        self.custo *= param


class Consumidores:
    pass


class Postos:

    def __init__(self):
        self.tanque = 0
        self.dist_cost = 0
        self.vizinhos = list()


    def comprar(self, custo):
        if self.tanque <= 200:
            self.tanque += 800
            self.dist_cost = custo

    def set_price(self):
        media = sum([i.preco for i in self.vizinhos]) / len(self.vizinhos)


if __name__ == '__main__':
    d1 = Distribuidores()
    c1 = Consumidores()
    p1 = Postos()
