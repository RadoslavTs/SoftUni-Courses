first_string = input()
second_string = input()
last_string = first_string
for sequence in range(len(first_string)):
    first_part = second_string[:sequence+1:]
    second_part = first_string[sequence+1:]
    resulting_string = first_part + second_part
    if resulting_string == last_string:
        continue
    print(resulting_string)
    last_string = resulting_string
