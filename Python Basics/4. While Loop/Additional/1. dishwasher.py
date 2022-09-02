bottle = int(input())
soap_quantity = bottle * 750
loops_count = 0
break_flag = False
plates_washed = int()
pots_washed = int()
while soap_quantity >= 0:
    dish_quantity = input()
    loops_count += 1
    if dish_quantity == "End":
        break_flag = True
        break
    if loops_count == 1 or loops_count == 2:
        soap_quantity -= int(dish_quantity) * 5
        plates_washed += int(dish_quantity)
    else:
        soap_quantity -= int(dish_quantity) * 15
        loops_count = 0
        pots_washed += int(dish_quantity)
if break_flag and soap_quantity >= 0:
    print("Detergent was enough!")
    print(f"{plates_washed} dishes and {pots_washed} pots were washed.")
    print(f"Leftover detergent {soap_quantity} ml.")
else:
    print(f"Not enough detergent, {abs(soap_quantity)} ml. more necessary!")

