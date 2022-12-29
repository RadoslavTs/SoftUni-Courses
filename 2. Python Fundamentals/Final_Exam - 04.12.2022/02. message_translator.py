import re

count_of_string = int(input())
pattern = r'!([A-Z][a-z]{2,})!:\[([A-za-z]{8,})\]'

for sequence in range(count_of_string):
    decoded_message = ''
    input_string = input()
    result = re.findall(pattern, input_string)
    if result:
        resulting_list = result[0]
        command = resulting_list[0]
        string_to_decode = resulting_list[1]
        for letter in string_to_decode:
            decoded_message += str(ord(letter)) + " "
        print(f"{command}: {decoded_message}")
    else:
        print("The message is invalid")
