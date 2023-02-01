def even_odd(*input_line):
    command = input_line[-1]

    if command == "even":
        return [n for n in input_line[:-1] if n % 2 == 0]
    else:
        return [n for n in input_line[:-1] if n % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))