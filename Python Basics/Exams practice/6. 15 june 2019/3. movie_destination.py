movie_budget = float(input())
destination = input()
season = input()
days_count = int(input())
daily_cost = 0
if destination == "Dubai":
    if season == "Winter":
        daily_cost = 45000
    else:
        daily_cost = 40000
elif destination == "Sofia":
    if season == "Winter":
        daily_cost = 17000
    else:
        daily_cost = 12500
else:
    if season == "Winter":
        daily_cost = 24000
    else:
        daily_cost = 20250
total_cost = daily_cost * days_count
if destination == "Dubai":
    total_cost *= 0.7
elif destination == "Sofia":
    total_cost *= 1.25
difference = abs(movie_budget - total_cost)
if movie_budget >= total_cost:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")