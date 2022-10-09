first_character = input()
second_character = input()
resulting_string = ""


for sequence in range(ord(first_character)+1, ord(second_character)):
    resulting_string += chr(sequence) + " "

print(resulting_string)


