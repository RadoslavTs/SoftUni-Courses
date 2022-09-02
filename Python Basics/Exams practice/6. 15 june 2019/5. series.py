budget = float(input())
series_count = int(input())
total_cost = 0
for sequence in range(series_count):
    series_name = input()
    series_price = float(input())
    if series_name == "Thrones":
        series_price *= 0.5
    elif series_name == "Lucifer":
        series_price *= 0.6
    elif series_name == "Protector":
        series_price *= 0.7
    elif series_name == "TotalDrama":
        series_price *= 0.8
    elif series_name == "Area":
        series_price *= 0.9
    total_cost += series_price
difference = abs(budget - total_cost)
if budget >= total_cost:
    print(f"You bought all the series and left with {difference:.2f} lv.")
else:
    print(f"You need {difference:.2f} lv. more to buy the series!")

