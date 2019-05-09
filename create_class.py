import random


class Animal:
    def __init__(self):
        self.money = 0

    def deposit(self, amount):
        self.money += amount


def create(f, n):
    res = list()
    for i in range(n):
        res.append(f())
    return res


def salaries(lst):
    for i in range(len(lst)):
        lst[i].deposit(5)


def interactions(lst_ag, lst_sh):
    for a in lst_ag:
        loja_vez = random.choice(lst_sh)
        # if loja_vez.capacidade() is True:
            # if a.checa_grana(loja_vez.cost) is True:
                # Guarda o custo da loja
                # Tira o dinheiro da conta do agente
                # Deposita na loja
                # REcolhe a satisfação
                # Retira um lugar da capacidade da loja
        pass


def main(num_dogs):
    bagulho = Animal()
    dogs = create(Animal, num_dogs)
    salaries(dogs)
    interactions(dogs, dogs)
    return dogs, dogs


if __name__ == '__main__':
    n = 3
    a, s = main(n)
