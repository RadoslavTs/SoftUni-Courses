def factorial(x, y):
    factorial_one = 1
    factorial_two = 1
    for sequence_one in range(1, int(x) + 1):
        factorial_one *= sequence_one
    for sequence_two in range(1, int(y) + 1):
        factorial_two *= sequence_two
    print(f"{(factorial_one/factorial_two):.2f}")


factorial(input(), input())