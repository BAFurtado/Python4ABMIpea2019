""" Exemplo de class
"""

# Começa com letra maiúscula
# Tem dois pontos e indentação. Normal.


class Abstract:

    # Sempre tem uma def __init__ que gera o objeto padrão
    def __init__(self):
        # Self refere-se a UMA instância do tipo da Classe Abstract
        self.variavel = 0
        self.minha_lista = list()
        self.meu_dict = dict()

    def metodo1(self):
        # Os métodos são exatamente como funções
        # Funcionam internamente as classes e alteram variáveis e estruturas

        # Por exemplo o método pode alterar o valor da variável
        self.variavel += 10

    def metodo2(self, x):
        # Outro método pode adicionar elementos a uma lista
        self.minha_lista.append(x)

    def metodo3(self, key, value):
        self.meu_dict[key] = value

    def __repr__(self):
        return 'Sou uma instãncia, minha variável contém {}'.format(self.variavel)


# Criando instâncias abstratas
minhas_instancias = list()
for i in range(4):
    minhas_instancias.append(Abstract())
    