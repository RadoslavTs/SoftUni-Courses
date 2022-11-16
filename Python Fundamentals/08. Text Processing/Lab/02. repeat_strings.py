input_list = input().split()
final_string = ""
for string_sequence in input_list:
    for sequence in range(len(string_sequence)):
        final_string += string_sequence
print(final_string)
