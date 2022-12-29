flower_type = input()
flower_count = int(input())
budget = int(input())
flower_cost = float()
difference = float()
if flower_type == "Roses":
    if flower_count > 80:
        flower_cost = flower_count * 5 * 0.9
    else:
        flower_cost = flower_count * 5
elif flower_type == "Dahlias":
    if flower_count > 90:
        flower_cost = flower_count * 3.80 * 0.85
    else:
        flower_cost = flower_count * 3.8
elif flower_type == "Tulips":
    if flower_count > 80:
        flower_cost = flower_count * 2.80 * 0.85
    else:
        flower_cost = flower_count * 2.80
elif flower_type == "Narcissus":
    if flower_count < 120:
        flower_cost = flower_count * 3 * 1.15
    else:
        flower_cost = flower_count * 3
else:
    if flower_count < 80:
        flower_cost = flower_count * 2.50 * 1.2
    else:
        flower_cost = flower_count * 2.50
difference = abs(budget - flower_cost)
if budget >= flower_cost:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")