movie_budget = float(input())
statists_count = int(input())
clothes_cost_per_statist = float(input())
movie_props = movie_budget * 0.1
total_clothes_cost = statists_count * clothes_cost_per_statist
discount = 0
if statists_count > 150:
    discount = total_clothes_cost * 0.1
total_cost = total_clothes_cost + movie_props - discount
difference = movie_budget - total_cost
if difference >= 0:
    print("Action!")
    print(f"Wingard starts filming with {abs(difference):.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {abs(difference):.2f} leva more.")