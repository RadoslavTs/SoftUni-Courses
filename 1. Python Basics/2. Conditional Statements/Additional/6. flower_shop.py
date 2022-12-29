import math
magnolia_count = int(input())
ziumbul_count = int(input())
roses_count = int(input())
cactus_count = int(input())
present_price = float(input())
magnolia_income = magnolia_count * 3.25
ziumbul_income = ziumbul_count * 4
roses_income = roses_count * 3.5
cactus_income = cactus_count * 8
total_income = ziumbul_income + magnolia_income + roses_income + cactus_income
tax = total_income * 0.05
net_income = total_income - tax
difference = net_income - present_price
if net_income >= present_price:
    print(f"She is left with {math.floor(difference)} leva.")
else:
    print(f"She will have to borrow {math.ceil(abs(difference))} leva." )