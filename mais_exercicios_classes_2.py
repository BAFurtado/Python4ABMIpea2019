""" Montar uma classe de CARTAS
    Seguindo Allen Doweny -- Think Python ch.18
    """

import random

# Passos
# 0. Entenda o início já explicitado abaixo
# 2. Next, vamos criar um baralho inteiro: DECK
# Crie uma classe Deck cuja __init__ é um nested for loop que armazena todas as cartas (todos os
# naipes e todos os ranks dentro de uma lista.
# 3. Crie um método em DECK que remove uma carta pop_card e retorna a carta removida
# 4. Crie um método que insere uma carta no Deck. add_card
# 5. Crie um método que embaralha (shuffle) as cartas
# 6. Volte ao Deck. Crie um método que move um n número de cartas (entre self e outro)
# 7. Crie uma class Hand que override o método __init__ do Deck e reinicia o self.cards
# como lista vazia


class Card:
    """ Classe de cartas. Na adaptação para o português, segue-se primeiro com o ranking
    e depois com o naipe.
    O naipe só segue de 0 a 3, na ordem especificada abaixo. Qualquer outra entrada, resulta
    em erro. """

    rank_names = [None, 'As', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Valete', 'Dama', 'Rei']
    naipes = ['Paus', 'Ouros', 'Copas', 'Espadas']

    def __init__(self, rank=4, naipe=0):
        self.rank = rank
        self.naipe = naipe

    def __lt__(self, other):
        t1 = self.naipe, self.rank
        t2 = other.naipe, other.rank
        return t1 < t2

    def __str__(self):
        return '{} de {}'.format(Card.rank_names[self.rank],
                                 Card.naipes[self.naipe])


class Deck:

    def __init__(self):
        """ Crie um Deck de 52 cartas
        """
        self.cards = list()
        for n in range(4):
            for r in range(1, 14):
                self.cards.append(Card(r, n))

    def pop_card(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def add_card(self, outra):
        self.cards.append(outra)

    def move_cards(self, outro, n):
        for c in range(n):
            outro.add_card(self.pop_card())


class Hand(Deck):
    def __init__(self):
        self.cards = list()


if __name__ == '__main__':
    # # zap = Card()
    # # valete = Card(11, 0)
    # # espadilha = Card(1, 3)
    # # sete_copas = Card(7, 2)
    # #
    # # print(zap < valete)
    # # print(valete < sete_copas)
    #
    # d = Deck()
    # print(len(d.cards))
    # d.shuffle()
    # # print(d.pop_card())
    # # print(len(d.cards))
    # # print(d.pop_card())
    # #
    # # d.add_card(zap)
    # # d.add_card(espadilha)
    # h = Hand()
    # print(len(h.cards))


    # Distribui 5 cartas para 4 jogadores
    morto = Deck()
    morto.shuffle()
    players = list()
    for i in range(4):
        players.append(Hand())
    for each in players:
        morto.move_cards(each, 5)

    print(len(morto.cards))
