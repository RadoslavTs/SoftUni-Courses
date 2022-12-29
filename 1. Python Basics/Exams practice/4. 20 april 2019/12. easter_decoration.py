customer_count = int(input())
baskets = 0
wreath = 0
chocolate_bunny = 0
item_counter = 0
client_price = 0
total_cost = 0
for sequence in range(customer_count):
    product = input()
    while product != "Finish":
        if product == "basket":
            baskets += 1
            item_counter += 1
        elif product == "wreath":
            wreath += 1
            item_counter += 1
        else:
            chocolate_bunny += 1
            item_counter += 1
        product = input()
    if item_counter % 2 == 0:
        client_price = (baskets * 1.5 + wreath * 3.8 + chocolate_bunny * 7) * 0.8
    else:
        client_price = baskets * 1.5 + wreath * 3.8 + chocolate_bunny * 7
    total_cost += client_price
    print(f"You purchased {item_counter} items for {client_price:.2f} leva.")
    client_price = 0
    baskets = 0
    wreath = 0
    chocolate_bunny = 0
    item_counter = 0
average_cost = total_cost / customer_count
print(f"Average bill per client is: {average_cost:.2f} leva.")

