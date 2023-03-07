from project.food.starter import Starter


class Soup(Starter):
    def __init__(self, name, price, grams):
        super().__init__(name, price, 0)
        self.__grams = grams

    @property
    def grams(self):
        return self.__grams
