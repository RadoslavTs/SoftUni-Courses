number_a = 1
number_b = 3
number_c = 0
number_d = 0
number = 123
result_flag = False
multiply = number_a * number_b * number_c * number_d
sum = number_a + number_b + number_c + number_d
result_one = multiply // sum
result_two = number % 3
print(result_one)
print(result_two)
if multiply // sum == 3 and number % 3 == 0:
    result_flag = True
print(result_flag)