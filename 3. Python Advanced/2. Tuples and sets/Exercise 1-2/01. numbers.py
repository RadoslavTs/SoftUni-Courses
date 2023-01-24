first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())
counter = int(input())
set_check = False
for sequence in range(counter):
    command = input().split()
    numbers = command[2:]

    if command[0] == "Add":
        if command[1] == "First":
            for num in numbers:
                first_set.add(int(num))
        elif command[1] == "Second":
            for num in numbers:
                second_set.add(int(num))

    elif command[0] == "Remove":
        if command[1] == "First":
            for num in numbers:
                first_set.discard(int(num))
        elif command[1] == "Second":
            for num in numbers:
                second_set.discard(int(num))

    elif command[0] == "Check":
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            set_check = True
        if set_check:
            print("True")
        else:
            print("False")

print(', '.join(map(str, sorted(first_set))))
print(*sorted(second_set), sep=', ')
