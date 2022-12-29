encrypted_message = input()
command = input()
while command != "Decode":
    command_split = command.split("|")
    action = command_split[0]
    if action == "Move":
        number_of_letters = int(command_split[1])
        letters_to_move = encrypted_message[:number_of_letters]
        encrypted_message = encrypted_message[number_of_letters:] + letters_to_move
    elif action == "Insert":
        index = int(command_split[1])
        value = command_split[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif action == "ChangeAll":
        substring = command_split[1]
        replacement = command_split[2]
        if substring in encrypted_message:
            encrypted_message = encrypted_message.replace(substring, replacement)
    command = input()
print(f"The decrypted message is: {encrypted_message}")
