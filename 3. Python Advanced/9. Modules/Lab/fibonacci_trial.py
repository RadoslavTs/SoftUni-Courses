import fibonacci

lst = []

command = input()

while command != 'Stop':
    command_split = command.split()
    action = command_split[0]
    if action == 'Create':
        number = int(command_split[2])
        lst = fibonacci.fibonacci_creator(number)
        print(f"{' '.join(str(x) for x in lst)}")
    elif action == 'Locate':
        number = int(command_split[1])
        print(fibonacci.index_return(lst, number))

    command = input()

