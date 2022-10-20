def positive_numbers(number):
    return [num for num in number if int(num) >= 0]


def negative_numbers(number):
    return [num for num in number if int(num) < 0]


def even_numbers(number):
    return [num for num in number if int(num) % 2 == 0]


def odd_numbers(number):
    return [num for num in number if int(num) % 2 != 0]


input_list = input().split(", ")
print("Positive: ", ", ".join(positive_numbers(input_list)))
print("Negative: ", ", ".join(negative_numbers(input_list)))
print("Even: ", ", ".join(even_numbers(input_list)))
print("Odd: ", ", ".join(odd_numbers(input_list)))
