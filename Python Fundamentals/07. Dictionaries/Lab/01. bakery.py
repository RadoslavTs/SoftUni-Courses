input_list = input().split()
bakery = {}
for sequence in range(0, len(input_list), 2):
    key = input_list[sequence]
    value = input_list[sequence + 1]
    bakery[key] = int(value)
print(bakery)
