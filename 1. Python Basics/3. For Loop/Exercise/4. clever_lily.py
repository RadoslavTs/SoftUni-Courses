age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
toy_quantity = int()
total_sum = float()
for sequence in range(1, age + 1):
    if sequence % 2 == 0:
        total_sum += sequence * 5 - 1
    else:
        toy_quantity += 1
income_from_toys = toy_quantity * toy_price
total_income = total_sum + income_from_toys
difference = abs(total_income - washing_machine_price)
if total_income >= washing_machine_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")