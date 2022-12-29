budget = float(input())
fuel_quantity_needed = float(input())
week_day = input()
fuel_cost = fuel_quantity_needed * 2.1
total_cost = fuel_cost + 100
if week_day == "Saturday":
    total_cost *= 0.9
else:
    total_cost *= 0.8
difference = abs(budget - total_cost)
if budget >= total_cost:
    print(f"Safari time! Money left: {difference:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {difference:.2f} lv.")