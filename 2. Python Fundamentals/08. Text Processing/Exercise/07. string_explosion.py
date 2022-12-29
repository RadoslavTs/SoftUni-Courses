input_text = input()
resulting_text = ""
strength = 0
for sequence in range(len(input_text)):
    if strength > 0 and input_text[sequence] != ">":
        strength -= 1
    elif input_text[sequence] == '>':
        resulting_text += input_text[sequence]
        strength += int(input_text[sequence+1])
    else:
        resulting_text += input_text[sequence]
print(resulting_text)
