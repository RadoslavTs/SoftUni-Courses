def loot_action(item):
    for subject in item:
        if subject not in initial_loot:
            initial_loot.insert(0, subject)
    return initial_loot


def drop_action(item):
    if 0 <= item < len(initial_loot):
        initial_loot.append(initial_loot.pop(item))
    return initial_loot


def steal_action(item):
    remove_list = []
    if item > len(initial_loot):
        remove_list = [objects for objects in initial_loot]
        initial_loot.clear()
    else:
        for sequence in range(item):
            remove_list.insert(0, initial_loot.pop())
    return remove_list, initial_loot


initial_loot = input().split("|")
data_info = input()
gained_treasure = 0
while data_info != "Yohoho!":
    command_list = data_info.split()
    command = command_list[0]
    if command == "Loot":
        item_list = [word for word in command_list if word != "Loot"]
        loot_action(item_list)
    elif command == "Drop":
        index_to_remove = int(command_list[1])
        drop_action(index_to_remove)
    elif command == "Steal":
        items_count = int(command_list[1])
        removing, initial_loot = steal_action(items_count)
        print(", ".join(removing))
    data_info = input()
for treasure in initial_loot:
    gained_treasure += len(treasure)
if len(initial_loot) > 0:
    total_treasure = gained_treasure / len(initial_loot)
    print(f"Average treasure gain: {total_treasure:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")


initial_loot = input().split("|")

data_info = input()

while data_info != "Yohoho!":
    command, *data = [x for x in data_info.split()]

    if command == "Loot":
        for item in data:
            if item not in initial_loot:
                initial_loot.insert(0, item)

    elif command == "Drop":
        index = int(data[0])
        if 0 <= index < len(initial_loot):
            initial_loot.append(initial_loot.pop(index))

    elif command == "Steal":
        count = int(data[0])
        stolen_items = initial_loot[-count:]
        initial_loot = initial_loot[:-count]
        print(*stolen_items, sep=", ")
    data_info = input()


if initial_loot:
    average_treasure_gain = sum(len(x) for x in initial_loot) / len(initial_loot)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")