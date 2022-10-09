product = input()
quantity = int(input())

coffee_price = 1.5
water_price = 1
coke_price = 1.4
snacks_price = 2
price = 0
if product == "coffee":
    price = coffee_price
elif product == "coke":
    price = coke_price
elif product == "water":
    price = water_price
else:
    price = snacks_price


def calculation(n):
    return lambda a: a * n


multiplier = calculation(price)
print(f"{multiplier(quantity):.2f}")
