food_quantity_bought = float(input())
hay_quantity_bought = float(input())
cover_quantity_bought = float(input())
guinea_weight = float(input())
food_quantity_remaining = food_quantity_bought
hay_quantity_remaining = hay_quantity_bought
covevr_quantity_remaining = cover_quantity_bought
days = 30
no_supplies_flag = False
for day in range(1, days+1):
    if food_quantity_remaining >= 0.3:
        food_quantity_remaining -= 0.3
        if food_quantity_remaining == 0:
            no_supplies_flag = True
    else:
        no_supplies_flag = True
        break
    if day % 2 == 0:
        if hay_quantity_remaining >= 0.05 * food_quantity_remaining:
            hay_quantity_remaining -= 0.05 * food_quantity_remaining
        else:
            no_supplies_flag = True
            break
    if day % 3 == 0:
        if covevr_quantity_remaining >= (1 / 3) * guinea_weight:
            covevr_quantity_remaining -= (1 / 3) * guinea_weight
        else:
            no_supplies_flag = True
            break
food_quantity_remaining = round(food_quantity_remaining, 4)
hay_quantity_remaining = round(hay_quantity_remaining, 4)
covevr_quantity_remaining = round(covevr_quantity_remaining, 4)
if food_quantity_remaining <=0 or hay_quantity_remaining <= 0 or covevr_quantity_remaining <= 0:
    no_supplies_flag = True
if no_supplies_flag:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_quantity_remaining:.2f}, Hay: {hay_quantity_remaining:.2f}, Cover: {covevr_quantity_remaining:.2f}.")