from math import ceil
number = int(input())
control_number = ceil(number / 2)
for i in range(1, number + 1):
    if i == 1 or i == number:
        print("*" * 2 * number + " " * number + "*" * 2 * number)
    else:
        if i == control_number:
            print("*" + "/" * (2 * number - 2) + "*" + "|" * number + "*" + "/" * (2 * number - 2) + "*")
        else:
            print("*" + "/" * (2 * number - 2) + "*" + " " * number + "*" + "/" * (2 * number - 2) + "*")