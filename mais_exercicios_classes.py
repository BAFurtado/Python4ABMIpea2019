"""
Objetivo: treinar mais classes
Específico: Fazer uma class que retorne tempo formatado

Source: Allen Downey -- Think Python -- Unit 6
http://greenteapress.com/thinkpython2/code/
"""

# Passos
# 0. O python tem várias classes para horas, tempos e minutos
# A razão básica por detrás é a utilização de um número inteiro para tempo (em segundos) ou
# milisegundos. Aqui, o objetivo é apenas o  exercício da CLASSE em si.

# 1. Crie uma class Time()
# 2. A classe inicia-se com três variáveis hour, second e minute
# 3. Crie uma apresentação dos resultado com __str__ (ou __repr__)
# 4. Utilize a formatação '{:02d}:{:02d}:{:02d}'.format(h, m, s)
# 5. Adicione um método que some dois horários. A soma será feita individualmente:
# horas, minutos e segundos. Retorne o valor impresso
# 6. Adicione ao método anterior, funções que alterem minutos e segundos se estiverem passando
# ou forem iguais a 60 de modo que o resultado esteja legível
# 7. Conseguem pensar em outros métodos para adicionar?


class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    # def add_time(self, other):
    #     self.hour += other.hour
    #     self.minute += other.minute
    #     self.second += other.second
    #     self.round_to_60()
    #     print(self)

    def __add__(self, other):
        self.hour += other.hour
        self.minute += other.minute
        self.second += other.second
        self.round_to_60()
        print(self)
        return self

    def round_to_60(self):
        if self.second >= 60:
            mult = self.second // 60
            self.second -= 60 * mult
            self.minute += mult
        if self.minute >= 60:
            mult2 = self.minute // 60
            self.minute -= 60 * mult2
            self.hour += mult2

    def __str__(self):
        return '{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)


if __name__ == '__main__':
    t1 = Time(6, 58, 4)
    t2 = Time(19, 3, 5)
    t1 + t2
    t2 + t1
    t3 = t1 + t2
    t2 + t3 + t1
