class Person:
    __pi = 3.14

    def __init__(self, name):
        self.name = name



Person.__pi += 100
print(Person.__pi)
