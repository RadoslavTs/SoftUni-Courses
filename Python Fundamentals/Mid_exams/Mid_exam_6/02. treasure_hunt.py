def loot_action(item):
    for subject in item:
        if subject not in initial_loot:
            initial_loot.insert(0, subject)
    return initial_loot


def drop_action(item):
    if item < len(initial_loot):
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
command = input()
gained_treasure = 0
while command != "Yohoho!":
    command_list = command.split()
    action = command_list[0]
    if action == "Loot":
        item_list = [word for word in command_list if word != "Loot"]
        loot_action(item_list)
    elif action == "Drop":
        index_to_remove = int(command_list[1])
        drop_action(index_to_remove)
    elif action == "Steal":
        items_count = int(command_list[1])
        removing, initial_loot = steal_action(items_count)
        print(", ".join(removing))
    command = input()
for treasure in initial_loot:
    gained_treasure += len(treasure)
if len(initial_loot) > 0:
    total_treasure = gained_treasure / len(initial_loot)
    print(f"Average treasure gain: {total_treasure:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")

