def even_odd(*input_line):
    checks = []
    for input in input_line:
        if type(input) == int:
            checks.append(input)
    command = input_line[-1]

    even = []
    odd = []
    for num in checks:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    if command == "even":
        return even
    else:
        return odd


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))