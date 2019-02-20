""" Class template
    Ipea's Python for agent-based modeling course
    """

import random


# class name typically Capital letter
class Template:

    # Usually has an __init__ method called at the moment of instance creation
    def __init__(self, name, arg1, arg2):

        # Armazena os parâmetros de início dentro daquela instância
        # É comum ter uma ID de identificação única, ou nome
        self.id = name
        self.arg1 = arg1
        self.arg2 = arg2

        # Pode conter containers, data structures
        self.members = dict()
        self.ranking = list()

        # Ou ainda, um valor randômico
        self.luck = random.randrange(1, 60)

    def method1(self, quantia):
        # Modifica um valor armazenado
        self.arg1 += quantia

    def method2(self, outro_agente):
        # Pode comparar-se com outro agente e acessar métodos do outro agente
        if self.arg1 > outro_agente.arg1:
            return True
        else:
            return False

    def method3(self):
        # Um método pode acessar um outro método.
        # Nesse caso, adicionando um valor aleatório ao arg1!
        self.method1(self.luck)


if __name__ == '__main__':
    # Sempre TESTE
    a = Template(1, 23, 50)
    b = Template(0, 50, 23)
    a.method1(25)
    print(b.method2(a))
    print('Your lucky number is {}'.format(b.luck))
    print('Your account increased by {}'.format(b.luck))
