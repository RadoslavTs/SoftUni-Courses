def shop_from_grocery_list(budget, grocery_list, *price_list):
    shopping_cart = []
    for item in price_list:
        item_name = item[0]
        item_price = float(item[1])
        if item_price <= budget:
            if item_name not in grocery_list:
                continue
            elif item_name in shopping_cart:
                continue
            else:
                shopping_cart.append(item_name)
                budget -= item_price
                grocery_list.remove(item_name)

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
