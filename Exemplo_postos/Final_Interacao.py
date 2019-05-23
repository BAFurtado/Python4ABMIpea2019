from Final_Agentes import Distribuidores, Consumidores, Postos
import random


param = .1


def create(f, n):
    res = list()
    for j in range(n):
        res.append(f(j))
    return res


def vizinhanca(postos):
    for p in postos:
        # Trocar para questão das áreas
        p.add_vizinhos(random.choices(postos, k=4))


def main(postos, consum, distribuidor):
    # Adicionar vizinhos
    vizinhanca(postos)
    # Rodar os dias
    for d in range(100):
        # Carros consomem
        for carro in consum:
            carro.drive()
        # Distribuidora altera preços a cada 7 dias
        if d % 7 == 0:
            distribuidor.altera_custo(param)
        # Posto decide se compara gasolina
        # Posto modifica preço?
        # Consumidor verifica se compra gasolina




if __name__ == '__main__':
    # Listas
    lista_postos = create(Postos, 20)
    lista_consumidores = create(Consumidores, 1000)
    o_distribuidor = Distribuidores()
    main(lista_postos, lista_consumidores, o_distribuidor)
