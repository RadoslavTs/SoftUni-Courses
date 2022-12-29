input_string = input()
command = input()
password = ""
while command != "Done":
    command_split = command.split()
    action = command_split[0]
    if action == "TakeOdd":
        password = ""
        for sequence in range(len(input_string)):
            if sequence % 2 != 0:
                password += input_string[sequence]
        input_string = password
        print(input_string)
    elif action == "Cut":
        index = int(command_split[1])
        end_index = index + int(command_split[2])
        input_string = input_string[:index] + input_string[end_index:]
        print(input_string)
    elif action == "Substitute":
        substring = command_split[1]
        substitute = command_split[2]
        if substring in input_string:
            password = input_string.replace(substring, substitute)
            input_string = password
            print(input_string)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {input_string}")
