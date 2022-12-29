people_count = int(input())
season = input()
cost_per_person = 0
if people_count <= 5:
    if season == "spring":
        cost_per_person = 50
    elif season == "summer":
        cost_per_person = 48.5
    elif season == "autumn":
        cost_per_person = 60
    else:
        cost_per_person = 86
else:
    if season == "spring":
        cost_per_person = 48
    elif season == "summer":
        cost_per_person = 45
    elif season == "autumn":
        cost_per_person = 49.5
    else:
        cost_per_person = 85
total_cost = people_count * cost_per_person
if season == "summer":
    total_cost *= 0.85
elif season == "winter":
    total_cost *= 1.08
print(f"{total_cost:.2f} leva.")