product = input()
location = input()
count = float(input())
cost = float()
if location == "Sofia":
    if product == "coffee":
        cost = count * 0.5
    elif product == "water":
        cost = count * 0.8
    elif product == "beer":
        cost = count * 1.2
    elif product == "sweets":
        cost = count * 1.45
    else:
        cost = count * 1.6
elif location == "Plovdiv":
    if product == "coffee":
        cost = count * 0.4
    elif product == "water":
        cost = count * 0.7
    elif product == "beer":
        cost = count * 1.15
    elif product == "sweets":
        cost = count * 1.30
    else:
        cost = count * 1.5
else:
    if product == "coffee":
        cost = count * 0.45
    elif product == "water":
        cost = count * 0.7
    elif product == "beer":
        cost = count * 1.10
    elif product == "sweets":
        cost = count * 1.35
    else:
        cost = count * 1.55
print(cost)