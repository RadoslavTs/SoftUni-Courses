my_dictionary = {}
command = ""
while True:
    command = input()
    if command == "stop":
        break
    quantity = int(input())
    if command not in my_dictionary:
        my_dictionary[command] = 0
    my_dictionary[command] += quantity
for item in my_dictionary:
    print(f"{item} -> {my_dictionary[item]}")