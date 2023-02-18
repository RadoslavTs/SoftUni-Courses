from collections import deque


def stock_availability(product_list, action, *others):
    inventory = deque(product_list)
    if action == "delivery":
        for box in others:
            inventory.append(box)
    elif action == "sell":
        if others:
            if str(others[0]).isdigit():
                quantity_to_sell = int(others[0])
                for _ in range(quantity_to_sell):
                    inventory.popleft()
            else:
                for order in others:
                    if order in inventory:
                        while order in inventory:
                            inventory.remove(order)
        else:
            inventory.popleft()
    inventory = list(inventory)
    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
