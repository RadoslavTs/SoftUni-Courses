from project.animal import Animal


class Cheetah(Animal):
    EXPENSE = 60

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Cheetah.EXPENSE)