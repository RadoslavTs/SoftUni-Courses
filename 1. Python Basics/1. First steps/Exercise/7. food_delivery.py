chicken_order = int(input())
fish_order = int(input())
vegi_order = int(input())
chicken_pirce = chicken_order * 10.35
fish_price = fish_order * 12.4
vegi_price = vegi_order * 8.15
total_food = chicken_pirce + fish_price + vegi_price
desert = total_food * 0.2
delivery = 2.5
total_cost = total_food + desert + delivery
print(total_cost)
