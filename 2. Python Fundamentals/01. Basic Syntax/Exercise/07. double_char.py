string_name = input()
resulting_string = ""
while string_name != "End":
    for sequence in range(len(string_name)):
        resulting_string += 2 * string_name[sequence]
    if resulting_string != "SSooffttUUnnii":
        print(resulting_string)
    resulting_string = ""
    string_name = input()
