season = input()
group_type = input()
students_count = float(input())
night_count = float(input())
sport_type = str()
cost_per_night = float()
discount = 1
if season == "Winter":
    if group_type == "girls" or group_type == "boys":
        cost_per_night = 9.6
    elif group_type == "mixed":
        cost_per_night = 10
elif season == "Spring":
    if group_type == "girls" or group_type == "boys":
        cost_per_night = 7.2
    elif group_type == "mixed":
        cost_per_night = 9.5
else:
    if group_type == "girls" or group_type == "boys":
        cost_per_night = 15
    elif group_type == "mixed":
        cost_per_night = 20
if season == "Winter":
    if group_type == "girls":
        sport_type = "Gymnastics"
    elif group_type == "boys":
        sport_type = "Judo"
    else:
        sport_type = "Ski"
elif season == "Spring":
    if group_type == "girls":
        sport_type = "Athletics"
    elif group_type == "boys":
        sport_type = "Tennis"
    else:
        sport_type = "Cycling"
else:
    if group_type == "girls":
        sport_type = "Volleyball"
    elif group_type == "boys":
        sport_type = "Football"
    else:
        sport_type = "Swimming"
if students_count >= 50:
    discount = 0.5
elif students_count >= 20 and students_count < 50:
    discount = 0.85
elif students_count >= 10 and students_count < 20:
    discount = 0.95
cost = cost_per_night * students_count * night_count * discount
print(f"{sport_type} {cost:.2f} lv.")
