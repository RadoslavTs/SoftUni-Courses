fuel_type = input().lower()
fuel_quantity = int(input())
if fuel_type in ("gasoline diesel gas") and fuel_quantity >= 25:
    print(f"You have enough {fuel_type}.")
elif fuel_type in ("gasoline diesel gas") and fuel_quantity < 25:
    print(f"Fill your tank with {fuel_type}!")
else:
    print("Invalid fuel!")