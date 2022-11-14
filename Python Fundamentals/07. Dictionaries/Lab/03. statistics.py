command = input()
product_dictionary = {}
total_quantity = 0
while command != "statistics":
    command_list = command.split(": ")
    item = command_list[0]
    quantity = int(command_list[1])
    if item not in product_dictionary:
        product_dictionary[item] = quantity
    else:
        quantity += product_dictionary[item]
        product_dictionary[item] = quantity
    command = input()
print("Products in stock:")
for item in product_dictionary:
    print(f"- {item}: {product_dictionary[item]}")
print(f"Total Products: {len(product_dictionary)}")
print(f"Total Quantity: {sum(product_dictionary.values())}")
# for item in product_dictionary:
#     total_quantity += product_dictionary[item]
# print(f"Total Quantity: {total_quantity}")
