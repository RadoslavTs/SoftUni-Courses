input_string = input()
current_letter = ""
answer_string = []
for sequence in range(len(input_string)):
    current_letter = input_string[sequence]
    if current_letter.isupper():
        answer_string.append(sequence)
    current_letter = 0
print(answer_string)
