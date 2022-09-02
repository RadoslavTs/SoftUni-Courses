budget = float(input())
flour_price_kg = float(input())
egg_price_pack = flour_price_kg * 0.75
milk_price_per_liter = flour_price_kg * 1.25
loaf_of_bread_cost = egg_price_pack + flour_price_kg + (milk_price_per_liter / 4)
cooked_breads = 0
received_eggs = 0
third_bread = 0
while loaf_of_bread_cost <= budget:
    budget -= loaf_of_bread_cost
    cooked_breads += 1
    received_eggs += 3
    third_bread += 1
    if third_bread == 3:
        received_eggs -= (cooked_breads - 2)
        third_bread = 0
print(f"You made {cooked_breads} loaves of Easter bread! Now you have {received_eggs} eggs and {budget:.2f}BGN left.")
