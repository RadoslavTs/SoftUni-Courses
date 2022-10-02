number_of_lines = int(input())
input_list = []
balanced = True
temp_bracket = ""
for sequence in range(number_of_lines):
    input_line = input()
    if input_line == "(" or input_line == ")":
        input_list.append(input_line)
if input_list[0] != "(" and input_list[-1] != ")":
    balanced = False
for index in range(len(input_list) - 1):
    if input_list[index] == input_list[index + 1]:
        balanced = False
if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
