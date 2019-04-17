""" Exemplo de classe Animal """


class Animal:
    def __init__(self, name):
        self.name = name
        self.diet = None
        self.legs = 4
        self.age = 0

    def name(self):
        print(self.name)

    def set_diet(self, type):
        self.diet = type

    def change_legs(self, number):
        self.legs = number

    def get_old(self):
        self.age += 1

    def __repr__(self):
        return 'My name is {}'.format(self.name)


if __name__ == '__main__':
    a = Animal('Pooh')
    print(a)
    b = Animal('Mel')
    b.get_old()
    print(b.age)
    b.get_old()
    print(a.age)
    print(b.name)
    print('{} is {} years old'.format(b.name, b.age))
