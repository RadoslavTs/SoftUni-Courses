from math import ceil
number = int(input())
sequence = int()
after_dash = int()
mid_second = number - 4
if number % 2 == 0 and number > 3:
    sequence = number - 1
    mid_dash = 2
else:
    sequence = number
    mid_dash = 1
control_row = ceil(sequence / 2)
if number == 1:
    print("*")
elif number == 2:
    print("**")
else:
    for i in range(1, sequence + 1):
        if i == 1 or i == sequence:
            leftright = int((number - 1) / 2)
            stars = number - leftright * 2
            print("-" * leftright + "*" * stars + "-" * leftright)
        elif i == control_row:
            print("*" + "-" * (number - 2) + "*")
            after_dash = 1
        elif i < control_row:
            leftright_current = leftright - 1
            print("-" * leftright_current + "*" + "-" * mid_dash + "*" + "-" * leftright_current)
            mid_dash += 2
            leftright -= 1
        elif i > control_row and i < sequence + 1:
            leftright_second = leftright_current
            print("-" * after_dash + "*" + "-" * mid_second + "*" + "-" * after_dash)
            after_dash += 1
            mid_second -= 2
