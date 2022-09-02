drink_type = input()
sugar_request = input()
drinks_count = int(input())
drink_cost_before_discount = 0
if drink_type == "Espresso":
    if sugar_request == "Without":
        drink_cost_before_discount = drinks_count * 0.9
    elif sugar_request == "Normal":
        drink_cost_before_discount = drinks_count * 1
    else:
        drink_cost_before_discount = drinks_count * 1.2
elif drink_type == "Cappuccino":
    if sugar_request == "Without":
        drink_cost_before_discount = drinks_count * 1
    elif sugar_request == "Normal":
        drink_cost_before_discount = drinks_count * 1.2
    else:
        drink_cost_before_discount = drinks_count * 1.6
else:
    if sugar_request == "Without":
        drink_cost_before_discount = drinks_count * 0.5
    elif sugar_request == "Normal":
        drink_cost_before_discount = drinks_count * 0.6
    else:
        drink_cost_before_discount = drinks_count * 0.7
if sugar_request == "Without":
    drink_cost_before_discount *= 0.65
if drink_type == "Espresso" and drinks_count >= 5:
    drink_cost_before_discount *= 0.75
if drink_cost_before_discount > 15:
    drink_cost_before_discount *= 0.8
print(f"You bought {drinks_count} cups of {drink_type} for {drink_cost_before_discount:.2f} lv.")