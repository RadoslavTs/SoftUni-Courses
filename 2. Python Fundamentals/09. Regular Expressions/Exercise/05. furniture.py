import re

command = input()
search_term = r">>(\w+)<<(\d+[\.]?\d+)!(\d+)"
furniture_list = []
total_cost = 0
while command != "Purchase":
    search_result = re.search(search_term, command)
    if search_result:
        furniture, price, quantity = search_result.groups()
        furniture_list.append(furniture)
        total_cost += float(price) * int(quantity)
    command = input()

print("Bought furniture:")
if furniture_list:
    for element in furniture_list:
        print(element)
print(f"Total money spend: {total_cost:.2f}")
