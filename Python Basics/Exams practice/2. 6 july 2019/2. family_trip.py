budget = float(input())
nights_count = int(input())
night_price = float(input())
additional_expense_percentage = int(input())
additional_cost = additional_expense_percentage / 100 * budget
if nights_count > 7:
    night_price = night_price * 0.95
nights_total_cost = nights_count * night_price
total_cost = nights_total_cost + additional_cost
difference = abs(budget - total_cost)
if budget >= total_cost:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")