# Chama a biblioteca
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cria uma DataFrame, utilizando-se de um dicioário.
# Keys são column names
# Values, em listas, são os valores
data = pd.DataFrame({'col_a': [0, 1, 2, 3, 4, 5, 6, 7],
                     'col_b': [7, 6, 4, 2, 1, 1, 1, 0],
                     'strings': ['a', 'b', 'c', 9, 8, 7, np.nan, np.nan]})

# Exame dos dados
data.head()
data.tail()
data.info()
data.describe()
data.mean()
data.quantile(q=.9)
data.sum()
data.min()
data.max()


# Muito fácil de operar intercâmbio de dados.
# Para salvar para EXCEL, sempre inclua ponto e vírgula como separador
data.to_csv('nome_do_arquivo.csv', sep=';', index=False)
data.to_csv('nome_do_arquivo.csv', sep=';')

# Para ler o arquivo
data = pd.read_csv('nome_do_arquivo.csv', sep=';', index_col=False)
data = pd.read_csv('nome_do_arquivo.csv', sep=';')

# Para deletar uma coluna

data = data.drop('Unnamed: 0', axis=1)

# Identificar nomes colunas
data.columns

# Acessando colunas especificas
data.col_a.max()
data.col_b.sum()

# Alternativamente
data['col_a'].max()

# Seleciona linhas com valor maior que 3
t1 = data.loc[data.col_a > 3, 'col_a']
t2 = data.loc[data.col_a > 3, :]

t3 = data.loc[data.col_a > 3, 'col_b']
t4 = data.loc[data.strings == '8', 'col_b']

# Renaming columns
data.rename(columns={'col_a': 'col_a1'}, inplace=True)

# GroupBy e Sort Values
# Cortesia Professora Débora Reis
# df.groupby(["coluna"]).coluna.funcao()` : para executar uma função em uma coluna
# df.groupby(["coluna1", "coluna2"]).coluna.funcao()` : para executar uma função em multiplas colunas
# f.groupby(["coluna"]).coluna.agg[[funcao1, funcao2])` : para executar multiplas funções em uma coluna
# df.sort_values(by="coluna", ascending=False)`: para ordenar uma coluna do maior valor para o menor
# df.sort_values(by=["coluna1","coluna2"])`: para ordenar por mais de uma coluna

data = data.sort_values(by='col_b', ascending=True)
data.groupby(by='col_b').col_b.agg(['sum', 'count'])

# Para plotar direto do DataFrame

data.col_a1.plot(kind='hist')
plt.show()

