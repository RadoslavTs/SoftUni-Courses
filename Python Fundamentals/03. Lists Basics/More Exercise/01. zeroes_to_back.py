input_list = input().split(", ")
output_list = []
for dublication in input_list:
    output_list.append(int(dublication))
for sequence in input_list:
    if int(sequence) == 0:
        output_list.remove(int(sequence))
        output_list.append(int(sequence))
print(output_list)