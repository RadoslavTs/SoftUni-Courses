number = int(input())
banned = [",", ".", "_"]
pureness = True
for sequence in range(number):
    current_string = input()
    for letter in banned:
        if letter in current_string:
            pureness = False
            break
    if pureness:
        print(f"{current_string} is pure.")
    else:
        print(f"{current_string} is not pure!")
    pure = True
