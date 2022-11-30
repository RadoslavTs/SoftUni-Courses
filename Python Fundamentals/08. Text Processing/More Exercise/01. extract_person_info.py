number_of_lines = int(input())
for sequence in range(number_of_lines):
    input_line = input()
    name_start_index = input_line.index("@") + 1
    name_end_index = input_line.index("|")
    name = input_line[name_start_index:name_end_index]
    age_start_index = input_line.index("#") + 1
    age_end_index = input_line.index("*")
    age = input_line[age_start_index:age_end_index]
    print(f"{name} is {age} years old.")
