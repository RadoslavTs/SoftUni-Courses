def asci_function(x, y):
    characters = []
    for current_index in range(ord(x) + 1, ord(y)):
        characters.append(chr(current_index))
    return characters


first_character = input()
second_character = input()
resulting_string = ""
result = asci_function(first_character, second_character)
print(" ".join(result))


