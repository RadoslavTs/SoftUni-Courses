input_line = input()
while "\\" in input_line:
    index = input_line.index("\\")
    input_line = input_line[index::]
    if input_line[0] == "\\":
        input_line = input_line[1::]
resulting_list = input_line.split(".")
print(f"File name: {resulting_list[0]}")
print(f"File extension: {resulting_list[1]}")
