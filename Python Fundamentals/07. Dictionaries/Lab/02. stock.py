input_list = input().split()
dictionary_groceries = {}
for sequence in range(0, len(input_list), 2):
    key = input_list[sequence]
    value = input_list[sequence + 1]
    dictionary_groceries[key] = int(value)
looking_list = input().split()
for item in looking_list:
    if item in dictionary_groceries:
        print(f"We have {dictionary_groceries[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")