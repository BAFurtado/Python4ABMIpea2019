import random
from math import sqrt

params = {'percentual': .1}


class Firms:

    def __init__(self, combustible):
        self.volume = random.randrange(0, 10000)
        self.type = combustible
        self.distance = dict()
        self.loc = 0, 0
        self.price = 10
        self.custo_per_km = 10

    def calculate_price(self, market):
        if self.type == 'Etanol':
            self.price = market.calculate_distance(self.loc) * self.custo_per_km * (1 + market.tax)
        else:
            self.price = market.calculate_distance(self.loc) * self.custo_per_km


class Markets:
    def __init__(self, tax, loc, demanda):
        self.tax = tax
        self.loc = loc
        self.demanda = demanda
        self.volume = random.randrange(0, 10000)

    def calculate_distance(self, loc):
        # Recebe dicionário com a key: mercado e value: distância
        self.distance = sqrt((self.loc[0] - loc[0]) ** 2 + (self.loc[1] - loc[1]) ** 2)
        return self.distance

    def decision_buy(self):
        if self.volume - self.demanda < self.volume * params['percentual']:
            return True
        else:
            return False

    def buy(self, firm):
        self.volume += 2000
        firm.volume -= 2000

    def choose_firm(self, firms):
        chosen = random.choices(firms, k=3)
        if self.volume - self.demanda < self.volume * .5:
            self.buy(firms[0])
        else:
            # firma com preço mínimo
            preco_min = [x.preco for x in firms]


if __name__ == '__main__':
    f1 = Firms('Etanol')
    print(f1.type)

    m1 = Markets(.05, (0, 0), 5000)
    print(m1.calculate_distance((4, 3)))

