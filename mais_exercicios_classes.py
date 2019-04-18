"""
Objetivo: treinar mais classes
Específico: Fazer uma class que retorne tempo formatado

Source: Allen Downey -- Think Python -- Unit 6
"""

# Passos
# 0. O python tem várias classes para horas, tempos e minutos
# A razão básica por detrás é a utilização de um número inteiro para tempo (em segundos) ou
# milisegundos. Aqui, o objetivo é apenas o  exercício da CLASSE em si.

# 1. Crie uma class Time()
# 2. A classe inicia-se com três variáveis houe, second e minute
# 3. Crie uma apresentação dos resultado com __str__ (ou __repr__)
# 4. Utilize a formatação '{:02d}:{:02d}:{:02d}'.format(h, m, s)
# 5. Adicione um método que some dois horários. A soma será feita individualmente:
# horas, minutos e segundos. Retorne o valor impresso
# 6. Adicione ao método anterior, funções que alterem minutos e segundos se estiverem passando
# ou forem iguais a 60 de modo que o resultado esteja legível
# 7. Conseguem pensar em outros métodos para adicionar?
