""" Rápida demonstração gráficos
"""


# Sempre use a linha abaixo. É convenção Python
import matplotlib.pyplot as plt
import numpy as np

# Gerando dados aleatórios para trabalhar
x = np.random.randn(10000)

# 100 é o número de bins do histograma
plt.hist(x, 20, color='red')

# Note que aceita comandos tipo LaTeX -- entre símbolo dollar ($)
plt.title('Normal distribution with $\mu=0, \sigma=1$')
plt.savefig('meu_primeiro_histograma.png')
plt.show()

