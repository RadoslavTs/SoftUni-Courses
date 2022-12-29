number_of_commands = int(input())
my_dictionary = {}
for sequence in range(number_of_commands):
    command = input().split()
    command_action = command[0]
    name = command[1]
    license_plate_number = 0
    if command_action != "unregister":
        license_plate_number = command[2]
    if command_action == "register":
        if name not in my_dictionary:
            my_dictionary[name] = license_plate_number
            print(f"{name} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {my_dictionary[name]}")
    else:
        if name not in my_dictionary:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del my_dictionary[name]
for key, value in my_dictionary.items():
    print(f"{key} => {value}")
