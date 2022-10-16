def factorial(digit):
    factorial_result = 1
    for sequence_one in range(1, int(digit) + 1):
        factorial_result *= sequence_one
    return factorial_result


number_one = int(input())
number_two = int(input())
result_one = factorial(number_one)
result_two = factorial(number_two)
result = result_one / result_two
print(f"{result:.2f}")