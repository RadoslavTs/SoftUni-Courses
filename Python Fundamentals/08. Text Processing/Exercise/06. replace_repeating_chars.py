input_text = input()
resulting_string = ""
last_added_letter = ""
for sequence in range(len(input_text)):
    if sequence == 0:
        resulting_string += input_text[sequence]
        last_added_letter = input_text[sequence]
    else:
        if last_added_letter == input_text[sequence]:
            continue
        else:
            resulting_string += input_text[sequence]
            last_added_letter = input_text[sequence]
print(resulting_string)
