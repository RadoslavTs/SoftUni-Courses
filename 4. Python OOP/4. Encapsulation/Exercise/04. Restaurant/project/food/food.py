from project.product import Product


class Food(Product):
    def __init__(self, name, price, grams):
        super().__init__(name, price)
        self.__grams: float = grams

    @property
    def milliliters(self):
        return self.__grams
