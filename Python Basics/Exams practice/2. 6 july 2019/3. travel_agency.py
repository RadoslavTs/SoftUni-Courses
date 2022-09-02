city_destination = input()
cities = ["Bansko", "Borovets", "Varna", "Burgas"]
package_types = ["noEquipment", "withEquipment", "noBreakfast", "withBreakfast"]
package_type = input()
vip_card = input()
nights_count = int(input())
night_price = 0
if nights_count < 1:
    print("Days must be positive number!")
elif city_destination not in cities or package_type not in package_types:
    print("Invalid input!")
else:
    if nights_count > 7:
        nights_count -= 1
    if city_destination == "Bansko" or city_destination == "Borovets":
        if package_type == "withEquipment":
            if vip_card == "yes":
                night_price = 100 * 0.9
            else:
                night_price = 100
        else:
            if vip_card == "yes":
                night_price = 80 * 0.95
            else:
                night_price = 80
    else:
        if package_type == "withBreakfast":
            if vip_card == "yes":
                night_price = 130 * 0.88
            else:
                night_price = 130
        else:
            if vip_card == "yes":
                night_price = 100 * 0.93
            else:
                night_price = 100
    total_cost = night_price * nights_count
    print(f"The price is {total_cost:.2f}lv! Have a nice time!")


