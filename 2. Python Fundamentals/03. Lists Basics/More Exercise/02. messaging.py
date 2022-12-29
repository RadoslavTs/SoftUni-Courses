number_sequence = input().split()
input_string = input()
temp_input_string = ""
output_string = ""
temp_key = 0
for key_number in number_sequence:
    for sequence in range(len(key_number)):
        temp_key += int(key_number[sequence])
    while temp_key >= len(input_string):
        temp_key -= len(input_string)
    output_string += input_string[temp_key]
    input_string = input_string[0:temp_key:] + input_string[temp_key + 1::]
    temp_key = 0
print(output_string)
