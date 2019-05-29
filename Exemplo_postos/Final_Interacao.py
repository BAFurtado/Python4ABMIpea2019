from Final_Agentes import Distribuidores, Consumidores, Postos
import random


param = random.randrange(-10, 10) / 100


def create(f, n):
    res = list()
    for j in range(n):
        res.append(f(j))
    return res


def vizinhanca(postos):
    for p in postos:
        # Trocar para questão das áreas
        p.add_vizinhos(random.choices(postos, k=4))

"""
def abastece (list_cons, list_posto):
    for d in range(120):
        # carros testma nível de combustivel
        # carros escolhem melhor preço e abastecem
        # Carros consomem
        for carro in consum:
            if check_gas(carro) == False:
                posto_vez = min(random.choices(list_posto, 3)
                posto_vez.tanque -= 60 - carro.level_gas
                carro.level_gas = 60                          
            else:
                carro.drive()

def estatisticas(dist, posto):
    prdist = []
    prcons = []
    prposto = []
    for d in range(120):
        prdist.append(dist.custo)
        for each in posto:
            prcons.append
"""


def main_func(postos, consum, distribuidor):
    # Recebe postos e consumidores
    # Adicionar vizinhos
    vizinhanca(postos)
    # Rodar os dias
    for d in range(120):
        #carros testma nível de combustivel
        #carros escolhem melhor preço e abastecem
        # Carros consomem
        # LISTA POSTOS, LISTA CONSUMIDORES = ABASTECE(LIS1, LIS2)
        for carro in consum:
            if carro.check_gas() is True:
                postos_aconferir = random.sample(lista_postos, 3)
                # Retornar o posto com preço mínimo.
                posto_vez = 5
                posto_vez.tanque -= (60 - carro.level_gas)
                carro.add_gas()
                carro.drive()
            else:
                carro.drive()

        # Distribuidora altera preços a cada 7 dias
        if d % 7 == 0:
            distribuidor.altera_custo(param)

        # Posto decide se compara gasolina
        for loja in postos:
            if loja.check_estoque is True:
                loja.tanque = 1000
                loja.set_price(distribuidor.custo)
        return lista_postos, lista_consumidores, distribuidor

        #Obtém preços



        # Posto modifica preço?
        # Consumidor verifica se compra gasolina




if __name__ == '__main__':
    # Listas
    lista_postos = create(Postos, 20)
    lista_consumidores = create(Consumidores, 1000)
    o_distribuidor = Distribuidores()
    main_func(lista_postos, lista_consumidores, o_distribuidor)
