my_string = input()
string_to_list = my_string.split(" ")
resulting_string = []
for sequence in range(len(string_to_list)):
    resulting_string.append(int(string_to_list[sequence]) * -1)
print(resulting_string)