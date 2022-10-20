def collect_action(objects):
    if objects not in journal:
        journal.append(objects)
    return journal


def drop_action(objects):
    if objects in journal:
        journal.remove(objects)
    return journal


def combine_action(first_thing, second_thing):
    if first_thing in journal:
        index_to_insert = journal.index(first_thing)
        journal.insert(index_to_insert+1, second_thing)
    return journal


def renew_action(objects):
    if objects in journal:
        pop_index = journal.index(objects)
        journal.append(journal.pop(pop_index))
    return journal


journal = input().split(", ")
command = input()
while command != "Craft!":
    command_split = command.split(" - ")
    action = command_split[0]
    item = command_split[1]
    if action == "Collect":
        collect_action(item)
    elif action == "Drop":
        drop_action(item)
    elif action == "Combine Items":
        item_list = item.split(":")
        first_item = item_list[0]
        second_item = item_list[1]
        combine_action(first_item, second_item)
    elif action == "Renew":
        renew_action(item)
    command = input()
print(", ".join(journal))