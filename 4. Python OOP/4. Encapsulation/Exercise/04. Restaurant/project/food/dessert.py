from project.food.food import Food


class Dessert(Food):
    def __init__(self, name, price, calories):
        super().__init__(name, price, 0)
        self.__calories: float = calories

    @property
    def calories(self):
        return self.__calories