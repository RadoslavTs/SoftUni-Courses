secret_message = input()
command = input()
while command != "Reveal":
    command_split = command.split(":|:")
    command_type = command_split[0]
    if command_type == "InsertSpace":
        index_to_insert = int(command_split[1])
        secret_message = secret_message[:index_to_insert] + " " + secret_message[index_to_insert:]
        print(secret_message)
    elif command_type == "Reverse":
        substring_reverse = command_split[1]
        if substring_reverse in secret_message:
            replacement_reverse = substring_reverse[::-1]
            secret_message = secret_message.replace(substring_reverse, "", 1)
            secret_message += replacement_reverse
            print(secret_message)
        else:
            print("error")
    elif command_type == "ChangeAll":
        substring = command_split[1]
        replacement = command_split[2]
        secret_message = secret_message.replace(substring, replacement)
        print(secret_message)
    command = input()

print(f"You have a new text message: {secret_message}")
