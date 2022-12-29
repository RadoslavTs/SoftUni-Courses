# def multiply(a, b):
#     return a * b


#
# def divide(a, b):
#     return a / b
#
#
# def add(a, b):
#     return a + b
#
#
# def subtract(a, b):
#     return a - b
#
# operator = input()
# number_one = int(input())
# number_two = int(input())
#
# if operator == "multiply":
#     print(multiply(number_one, number_two))
# elif operator == "divide":
#     print(f"{divide(number_one, number_two):.0f}")
# elif operator == "add":
#     print(add(number_one, number_two))
# else:
#     print(subtract(number_one, number_two))

import operator


def calculations(number_a, number_b, operation):
    operations_dict = {"multiply": operator.mul, "divide": operator.truediv, "add": operator.add,
                       "subtract": operator.sub}
    return int(operations_dict[operation](number_a, number_b))


type_of_operation = input()
first_number = int(input())
second_number = int(input())
print(calculations(first_number, second_number, type_of_operation))
