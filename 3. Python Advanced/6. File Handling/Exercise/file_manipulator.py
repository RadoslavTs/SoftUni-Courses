import os
command = input()

while command != "End":
    command_split = command.split('-')
    action = command_split[0]
    file_name = command_split[1]

    if action == "Create":
        file = open(file_name, 'w')
        file.close()

    elif action == "Add":
        content = command_split[2]
        with open(file_name, 'a') as file:
            file.write(f'{content}\n')

    elif action == "Replace":
        text_to_replace = command_split[2]
        replacement_text = command_split[3]
        try:
            with open(file_name, 'r') as source:
                source_data = source.read()

            source_data = source_data.replace(text_to_replace, replacement_text)

            with open(file_name, 'w') as file:
                file.write(''.join(source_data))

        except FileNotFoundError:
            print("An error occurred")

    elif action == "Delete":
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")

    command = input()

