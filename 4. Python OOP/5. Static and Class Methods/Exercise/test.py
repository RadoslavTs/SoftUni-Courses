from functools import reduce


class Calculator:

    @staticmethod
    def addition(lst):
        return reduce(lambda a, b: a + b, lst)


print(Calculator.addition([1, 2, 3, 4]))