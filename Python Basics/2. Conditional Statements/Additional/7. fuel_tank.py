fuel_type = input()
current_fuel_quantity = float(input())
diesel_fuel = "diesel"
gasoline_fuel = "gasoline"
gas_fuel = "gas"
if fuel_type == "Diesel":
    if current_fuel_quantity >= 25:
        print(f"You have enough {diesel_fuel}.")
    else:
        print(f"Fill your tank with {diesel_fuel}!")
elif fuel_type == "Gasoline":
    if current_fuel_quantity >= 25:
        print(f"You have enough {gasoline_fuel}.")
    else:
        print(f"Fill your tank with {gasoline_fuel}!")
elif fuel_type == "Gas":
    if current_fuel_quantity >= 25:
        print(f"You have enough {gas_fuel}.")
    else:
        print(f"Fill your tank with {gas_fuel}!")
else:
    print("Invalid fuel!")
