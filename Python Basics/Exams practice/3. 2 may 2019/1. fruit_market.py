strawberry_price = float(input())
banana_quantity = float(input())
orange_quantity = float(input())
malini_quantity = float(input())
strawberry_quantity = float(input())
malini_price = strawberry_price * 0.5
strawberry_cost = strawberry_quantity * strawberry_price
malini_cost = malini_quantity * malini_price
orance_price = malini_price * 0.6
orange_cost = orange_quantity * orance_price
banana_price = malini_price * 0.2
banana_cost = banana_price * banana_quantity
total_cost = banana_cost + orange_cost + malini_cost + strawberry_cost
print(f"{total_cost:.2f}")