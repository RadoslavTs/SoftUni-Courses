def urgent_action(item):
    if item not in categories:
        categories.insert(0, item)
    return categories


def unnecessary_action(item):
    if item in categories:
        categories.remove(item)
    return categories


def correct_action(item_one, item_two):
    if item_one in categories:
        index_change = categories.index(item_one)
        categories[index_change] = item_two
    return categories


def rearrange_action(item):
    if item in categories:
        item_index = categories.index(item)
        categories.append(categories.pop(item_index))
    return categories


categories = input().split("!")
command = input()
while command != "Go Shopping!":
    command_list = command.split()
    action = command_list[0]
    first_item = command_list[1]
    if len(command_list) > 2:
        second_item = command_list[2]
    if action == "Urgent":
        urgent_action(first_item)
    elif action == "Unnecessary":
        unnecessary_action(first_item)
    elif action == "Correct":
        correct_action(first_item, second_item)
    elif action == "Rearrange":
        rearrange_action(first_item)
    command = input()
print(", ".join(categories))