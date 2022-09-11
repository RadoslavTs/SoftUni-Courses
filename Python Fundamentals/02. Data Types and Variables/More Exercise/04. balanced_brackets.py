number_of_lines = int(input())
first_bracket = False
second_bracket = False
middle_sector = False
for sequence in range(number_of_lines):
    input_line = input()
    if input_line == "(":
        first_bracket = True
