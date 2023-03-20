class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return 'meow'


class Dog(Animal):
    def make_sound(self):
        return "Bark"


class Chicken(Animal):
    def make_sound(self):
        return 'quack'


def animal_sound(animals: list):
    for animal in animals:
        if animal.species == 'cat':
            print('meow')
        elif animal.species == 'dog':
            print('woof-woof')


animals = [Cat('cat'), Dog('dog'), Chicken('Chicken')]
animal_sound(animals)