budget = float(input())
season = input()
type = str()
price = float()
car = str()
if budget <= 100:
    type = "Economy class"
    if season == "Summer":
        car = "Cabrio"
        price = budget * 0.35
    else:
        car = "Jeep"
        price = budget * 0.65
elif budget > 100 and budget <= 500:
    type = "Compact class"
    if season == "Summer":
        car = "Cabrio"
        price = budget * 0.45
    else:
        car = "Jeep"
        price = budget * 0.80
else:
    type = "Luxury class"
    car = "Jeep"
    price = budget * 0.9
print(type)
print(f"{car} - {price:.2f}")