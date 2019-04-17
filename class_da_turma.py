""" Exemplo de uma class construída coletivamente
"""


class Turma:
    def __init__(self, name='Python4ABMIpea'):
        self.name = name
        self.students = list()

    def add_student(self, name):
        self.students.append(name)

    def remove_student(self, name):
        self.students.remove(name)

    def count_std(self):
        return len(self.students)

    def list_std(self):
        for each in self.students:
            print(each)

    def __repr__(self):
        return '{} tem {} alunos'.format(self.name, self.count_std())


if __name__ == '__main__':
    a = Turma()
    print(type(a))
    print(a)
    a.add_student('Sissi')
    a.add_student('Esa Pekka')
    a.add_student('Gerson')
    a.add_student('Marlene')
    a.add_student('Rafael')
    a.add_student('Francirley')
    print(a)
    a.list_std()
    a.remove_student('Francirley')
    print(a)