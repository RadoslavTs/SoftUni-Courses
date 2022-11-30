raw_activation_key = input()
command = input()
activation_key = ""
while command != "Generate":
    command_split = command.split(">>>")
    action = command_split[0]
    if action == "Contains":
        substring = command_split[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
            command = input()
            continue
        else:
            print("Substring not found!")
            command = input()
            continue
    elif action == "Flip":
        direction = command_split[1]
        start_index = int(command_split[2])
        end_index = int(command_split[3])
        string_to_change = raw_activation_key[start_index:end_index]
        if direction == "Upper":
            string_to_change = string_to_change.upper()
        elif direction == "Lower":
            string_to_change = string_to_change.lower()
        raw_activation_key = raw_activation_key[:start_index] + string_to_change + raw_activation_key[end_index:]
        print(raw_activation_key)
    elif action == "Slice":
        start_index = int(command_split[1])
        end_index = int(command_split[2])
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)
    command = input()
print(f"Your activation key is: {raw_activation_key}")
