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
    def __init__(self, i):
        self.id = i
        self.capacity = 60
        self.level_gas = self.capacity * random.random()

    def add_gas(self):
        #volume = 60 - self.level_gas
        self.level_gas = 60

    def drive(self):
        self.level_gas -= 6

    def check_gas(self):
        if self.level_gas <= 0.2 * self.capacity:
            print('Go to the gas station')
            return True
        else:
            print('Go ahead')
            return False

    #def bestprice(self):
        #self



class Postos:
    def __init__(self, p, area=None, vizinhos=None):
        self.identity = p
        self.tanque = random.randrange(200, 1000)
        self.dist_cost = 10
        self.loc = area
        self.vizinhos = vizinhos
        self.preco = 10

    def check_estoque(self):
        if self.tanque <= 200:
            return True
        else:
            return False

    #def comprar(self, custo):
    #    if self.tanque <= 200:
    #        self.tanque += 1000 - self.tanque
    #        self.dist_cost = custo

    def add_vizinhos(self, viz):
        self.vizinhos = viz

    def set_distr_cost(self, preco):
        self.dist_cost = preco

    def set_price(self):
        preco_vizinho = min([i.preco for i in self.vizinhos])
        preco_posto = self.dist_cost * 1.05
        if preco_posto > 1.05 * preco_vizinho:
            preco_posto = preco_vizinho * (1 + (random.randrange(0, 5) / 100))
        return preco_posto


if __name__ == '__main__':
    d = Distribuidores()
    c = Consumidores(1)
    p1 = Postos(2)
    p2 = Postos(3)
    p3 = Postos(4)
    viz = [p2, p3]
    c.check_gas()
    p1.add_vizinhos(viz)
    print('preço', p1.set_price())
    print(p1.tanque, c.level_gas)
