""" Segundo exemplo
"""


# Sempre use a linha abaixo. É convenção Python
import matplotlib.pyplot as plt
import numpy as np

fig1 = plt.figure()  # an empty figure with no axes

x = np.linspace(0, 2, 100)

# plt.plot(x, x, label='linear', color='black')
# plt.plot(x, x**2, label='quadratic', color='pink')
# plt.plot(x, x**3, label='cubic', color='brown')
#
# plt.xlabel('x label')
# plt.ylabel('y label')
#
# plt.title("Simple Plot")
# plt.legend()
# plt.show()

# Outro gráfico. Esse é o caso padrão, cria-se a figura e as modificações se dão no ax/axes
#
# x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig2, ax = plt.subplots()
ax.plot(x, y)
plt.show()
