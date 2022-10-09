def sum_numbers(a, b):
    return a + b


def subtract(a, b):
    return a - b


def add_and_subtract(a, b, c):
    pass

number_one = int(input())
number_two = int(input())
number_three = int(input())
sum_result = sum_numbers(number_one, number_two)
print(subtract(sum_result, number_three))