input_list = input().split()
my_dictionary = {"shards": 0, "fragments": 0, "motes": 0}
epic_list = ["shards", "fragments", "motes"]
legendary_flag = False
while not legendary_flag:
    for sequence in range(0, len(input_list), 2):
        quantity = input_list[sequence]
        item = input_list[sequence+1].lower()
        if item not in my_dictionary:
            my_dictionary[item] = 0
        my_dictionary[item] += int(quantity)
        if item == "shards":
            if my_dictionary[item] >= 250:
                print("Shadowmourne obtained!")
                legendary_flag = True
                my_dictionary[item] -= 250
                break
        elif item == "fragments":
            if my_dictionary[item] >= 250:
                print("Valanyr obtained!")
                legendary_flag = True
                my_dictionary[item] -= 250
                break
        elif item == "motes":
            if my_dictionary[item] >= 250:
                print("Dragonwrath obtained!")
                legendary_flag = True
                my_dictionary[item] -= 250
                break
    input_list = input().split()
print(f"shards: {my_dictionary['shards']}")
print(f"fragments: {my_dictionary['fragments']}")
print(f"motes: {my_dictionary['motes']}")
for key, value in my_dictionary.items():
    if key not in epic_list:
        print(f"{key}: {value}")
