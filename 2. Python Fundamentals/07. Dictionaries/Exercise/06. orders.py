input_line = input().split()
my_dictionary = {}
while len(input_line) > 1:
    item, price, quantity = input_line[0], float(input_line[1]), int(input_line[2])
    if item not in my_dictionary:
        my_dictionary[item] = []
        my_dictionary[item].append(0)
        my_dictionary[item].append(0)
    my_dictionary[item][0] = price
    my_dictionary[item][1] += quantity
    input_line = input().split()
for item in my_dictionary:
    total = my_dictionary[item][0] * my_dictionary[item][1]
    print(f"{item} -> {total:.2f}")
