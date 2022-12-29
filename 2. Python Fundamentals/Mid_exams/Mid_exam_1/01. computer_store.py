command = input()
cost_before_tax = 0
invalid_order = False
while command != "special" and command != "regular":
    if float(command) < 0:
        print("Invalid order!")
        continue
    cost_before_tax += float(command)
    command = input()
cost_after_tax = cost_before_tax * 1.2
tax = cost_before_tax * 0.2
if command == "special":
    cost_after_tax *= 0.9
if cost_before_tax == 0:
    invalid_order = True
if not invalid_order:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {cost_before_tax:.2f}$")
    print(f"Taxes: {tax:.2f}$")
    print("-----------")
    print(f"Total price: {cost_after_tax:.2f}$")
else:
    print("Invalid order!")
