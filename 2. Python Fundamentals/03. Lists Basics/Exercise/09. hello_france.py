collection_of_items = input().split("|")
budget = float(input())
bought_list = []
initial_budget = budget
sold_list = []
sold_list_string = ""
profit = float()
for splitting in collection_of_items:
    split_items = splitting.split("->")
    item = split_items[0]
    price = float(split_items[1])
    if item == "Clothes":
        if price > 50:
            pass
        else:
            if budget < price:
                pass
            else:
                budget -= price
                bought_list.append(price)
    elif item == "Shoes":
        if price > 35:
            pass
        else:
            if budget < price:
                pass
            else:
                budget -= price
                bought_list.append(price)
    if item == "Accessories":
        if price > 20.5:
            pass
        else:
            if budget < price:
                pass
            else:
                budget -= price
                bought_list.append(price)
for bought in bought_list:
    sold_list.append(float(bought) * 1.4)
    profit += float(bought) * 0.4
for sold_string in sold_list:
    format_string = "{:.2f}".format(sold_string)
    sold_list_string += str(format_string) + " "
print(sold_list_string)
print(f"Profit: {profit:.2f}")
for ticket in bought_list:
    budget -= float(ticket)
budget = profit + initial_budget
if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")