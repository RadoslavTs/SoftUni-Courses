target_revenue = float(input())
cocktail_name = input()
accumulated_sum = 0
order_cost = 0
while cocktail_name != "Party!":
    cocktail_number = int(input())
    cocktail_price = len(cocktail_name)
    order_cost = cocktail_price * cocktail_number
    if order_cost % 2 != 0:
        order_cost = order_cost * 0.75
    accumulated_sum += order_cost
    if accumulated_sum >= target_revenue:
        break
    order_cost = 0
    cocktail_name = input()
difference = abs(target_revenue - accumulated_sum)
if accumulated_sum < target_revenue:
    print(f"We need {difference:.2f} leva more.")
else:
    print("Target acquired.")
print(f"Club income - {accumulated_sum:.2f} leva.")
