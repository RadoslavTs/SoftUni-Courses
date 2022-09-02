number = int(input())
banned = [",", ".", "_", "h"]
pure = True
for sequence in range(number):
    string_name = input()
    for letter in banned:
        if letter in string_name:
            pure = False
            break
    if pure:
        print("string is pure")
if not pure:
    print("string is not pure")