from math import ceil
guest_count = int(input())
budget = float(input())
kozunak_needed = ceil(guest_count / 3)
eggs_needed = guest_count * 2
kozunak_cost = kozunak_needed * 4
eggs_cost = eggs_needed * 0.45
total_cost = kozunak_cost + eggs_cost
difference = abs(budget - total_cost)
if budget >= total_cost:
    print(f"Lyubo bought {kozunak_needed} Easter bread and {eggs_needed} eggs.")
    print(f"He has {difference:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {difference:.2f} lv. more.")
