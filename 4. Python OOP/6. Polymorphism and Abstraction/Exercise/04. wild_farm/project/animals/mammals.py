from project.animals.animal import Animal, Bird, Mammal
from abc import ABC, abstractmethod

from project.food import Meat, Fruit, Vegetable


class Mouse(Mammal):
    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def food_that_eats(self):
        return [Fruit, Vegetable]

    @property
    def gained_weight(self):
        return 0.1


class Dog(Mammal):
    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.4


class Cat(Mammal):
    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def food_that_eats(self):
        return [Meat, Vegetable]

    @property
    def gained_weight(self):
        return 0.30


class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 1