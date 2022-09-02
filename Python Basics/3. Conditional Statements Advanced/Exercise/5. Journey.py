budget = float(input())
season = input()
location = str()
cost = float()
hotel = str()
if budget <= 100:
    if season == "summer":
        location = "Bulgaria"
        cost = budget * 0.3
    else:
        location = "Bulgaria"
        cost = budget * 0.7
elif budget <= 1000:
    if season == "summer":
        location = "Balkans"
        cost = budget * 0.4
    else:
        location = "Balkans"
        cost = budget * 0.8
else:
    location = "Europe"
    cost = budget * 0.9
if season == "summer" and location != "Europe":
    hotel = "Camp"
elif season == "winter" and location != "Europe":
    hotel = "Hotel"
else:
    hotel = "Hotel"
print(f"Somewhere in {location}")
print(f"{hotel} - {cost:.2f}")