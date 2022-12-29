fuel_type = input()
fuel_quantity = float(input())
club_card = input()
fuel_price = float()
total_cost = float()
discount = float()
if fuel_type == "Gasoline":
    if club_card == "No":
        fuel_price = 2.22
    else:
        fuel_price = 2.22 - 0.18
elif fuel_type == "Diesel":
    if club_card == "No":
        fuel_price = 2.33
    else:
        fuel_price = 2.33 - 0.12
elif fuel_type == "Gas":
    if club_card == "No":
        fuel_price = 0.93
    else:
        fuel_price = 0.93 - 0.08
total_cost = fuel_price * fuel_quantity
if fuel_quantity > 25:
    discount = total_cost * 0.1
elif fuel_quantity >= 20:
    discount = total_cost * 0.08
final_price = total_cost - discount
print(f"{final_price:.2f} lv.")

