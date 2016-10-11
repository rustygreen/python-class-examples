from datetime import datetime


class Animal:
    def __init__(self, name, color, animal_type):
        self.name = name
        self.color = color
        self.birthday = datetime.now()
        self.animal_type = animal_type
        self.tricks = ['bark']

    def age(self):
        return (datetime.now() - self.birthday).days

    def add_trick(self, trick):
        self.tricks.append(trick)

    def is_smart(self):
        return len(self.tricks) > 2

    def info(self):
        print('Hello, my name is ' + self.name + '. I am a ' + self.animal_type)


class Dog(Animal):
    def __init__(self, name, color, breed):
        Animal.__init__(self, name, color, 'dog')
        self.breed = breed

    def bark(self):
        print('Ruuuffff!')


class Cat(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name, color, 'cat')
        self.number_of_lives = 9

    def meow(self):
        print('Meowwww!')


fido = Dog('fido', 'black', 'black lab')
fido.add_trick('roll over')
fido.add_trick('play dead')
fido.add_trick('jump')
fido.info()

fido.bark()

spike = Cat('spike', 'tan')
spike.info()
spike.meow()







































# from datetime import datetime
#
# delta = datetime.now() - datetime(1985, 5, 8)
#
# print(delta.days/365)
# print(delta.days)
# print(delta.seconds)
# print(delta.microsecond)
# def secs_old(self):
#     return (datetime.now() - self.birthday).microseconds
