guest_count = int(input())
cost_per_guest = float(input())
budget = float(input())
if guest_count >= 10 and guest_count <= 15:
    cost_per_guest = cost_per_guest * 0.85
elif guest_count > 15 and guest_count <= 20:
    cost_per_guest = cost_per_guest * 0.8
elif guest_count > 20:
    cost_per_guest = cost_per_guest * 0.75
cake_price = budget * 0.1
total_guest_cost = guest_count * cost_per_guest
total_expense = total_guest_cost + cake_price
difference = abs(budget - total_expense)
if budget >= total_expense:
    print(f"It is party time! {difference:.2f} leva left.")
else:
    print(f"No party! {difference:.2f} leva needed.")