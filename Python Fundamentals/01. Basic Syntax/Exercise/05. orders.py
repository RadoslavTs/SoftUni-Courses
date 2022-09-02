orders_number = int(input())
coffee_price = 0
total = 0
for sequence in range(orders_number):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if (price_per_capsule < 0.01 or price_per_capsule > 100.00) or (days < 1 or days > 31) or (capsules_per_day < 1 or capsules_per_day > 2000):
        continue
    coffee_price = price_per_capsule * days * capsules_per_day
    total += coffee_price
    print(f"The price for the coffee is: ${coffee_price:.2f}")
print(f"Total: ${total:.2f}")