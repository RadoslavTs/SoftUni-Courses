from math import floor
from math import ceil
number = int(input())
roof_control = (number + 1) / 2
stars = int()
for i in range(1, number + 1):
    if number == 2:
        print("**")
        print("||")
        break
    if i <= roof_control:
        if i == 1 and number % 2 != 0:
            stars = 1
            stars_qty_one = int((number - stars) / 2)
            print("-" * stars_qty_one + "*" + "-" * stars_qty_one)
        elif i == 1 and number % 2 == 0:
            stars = 2
            stars_qty_two = int((number - stars) / 2)
            print("-" * stars_qty_two + "**" + "-" * stars_qty_two)
        else:
            stars += 2
            unders_score_qty = int((number - stars) / 2)
            print("-" * unders_score_qty + "*" * stars + "-" * unders_score_qty)
    if i > ceil(number / 2):
        if number - 2 > 0:
            print("|" + "*" * (number - 2) + "|")