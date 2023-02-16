def shopping_list(budget, **dict):
    bought_items = {}
    if budget >= 100:
        for item, (price, quant) in dict.items():
            if price * quant <= budget:
                if len(bought_items) < 5:
                    bought_items[item] = price * quant
                    budget -= (price * quant)

        return_string = ''
        for row in [f"You bought {item} for {price:.2f} leva.\n" for item, price in bought_items.items()]:
            return_string += row
    else:
        return_string = f"You do not have enough budget."
    return return_string


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
