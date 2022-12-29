budget = float(input())
statists_count = int(input())
statist_clothes_price = float(input())
decor_cost = budget * 0.1
statist_cost = statists_count * statist_clothes_price
if statists_count > 150:
    statist_cost = statist_cost * 0.9
total_cost = statist_cost + decor_cost
difference = abs(budget - total_cost)
if total_cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")