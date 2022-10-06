# numbers = list(map(float, input().split()))
# result = list(map(abs, numbers))
# print(result)

numbers = input().split()
float_numbers = list(map(float, numbers))

def absolute_values(number):
    return abs(number)

absolute_list = list(map(absolute_values, float_numbers))

print(absolute_list)