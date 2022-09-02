flour_price = float(input())
flour_qty = float(input())
sugar_qty = float(input())
eggs_qty = int(input())
east_qty = int(input())
sugar_price = flour_price * 0.75
eggs_price = flour_price * 1.1
east_price = sugar_price * 0.2
flour_cost = flour_price * flour_qty
sugar_cost = sugar_qty * sugar_price
eggs_cost = eggs_price * eggs_qty
east_cost = east_price * east_qty
total_cost = flour_cost + sugar_cost + eggs_cost + east_cost
print(f"{total_cost:.2f}")