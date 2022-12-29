starting_character = int(input())
finishing_character = int(input())
resulting_string = ""
for sequence in range(starting_character, finishing_character + 1):
    resulting_string += chr(sequence) + " "
print(resulting_string)