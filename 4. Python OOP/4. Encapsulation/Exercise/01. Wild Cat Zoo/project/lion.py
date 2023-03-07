from project.animal import Animal


class Lion(Animal):
    EXPENSE = 50

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Lion.EXPENSE)
