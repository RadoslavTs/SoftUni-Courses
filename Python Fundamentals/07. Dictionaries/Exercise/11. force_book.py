input_command = input()
my_dictionary = {}
while input_command != "Lumpawaroo":
    list_entry = input_command.split(" | ")
    if len(list_entry) == 1:
        list_entry = input_command.split(" -> ")
        force_user, force_side = list_entry[0], list_entry[1]
        if force_side not in my_dictionary:
            my_dictionary[force_side] = []
        for element in my_dictionary:
            if force_user in my_dictionary[element]:
                my_dictionary[element].remove(force_user)
                break
        my_dictionary[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    else:
        force_side, force_user = list_entry[0], list_entry[1]
        if force_side not in my_dictionary:
            my_dictionary[force_side] = []
        user_in = False
        for element in my_dictionary:
            if force_user in my_dictionary[element]:
                user_in = True
                break
        if not user_in:
            my_dictionary[force_side].append(force_user)
    input_command = input()
for element in my_dictionary:
    if len(my_dictionary[element]) > 0:
        print(f"Side: {element}, Members: {len(my_dictionary[element])}")
        for users in my_dictionary[element]:
            print(f"! {users}")
