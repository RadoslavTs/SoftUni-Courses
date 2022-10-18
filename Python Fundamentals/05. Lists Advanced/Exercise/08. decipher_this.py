input_list = input().split()
final_list = []
for word in input_list:
    digits = int("".join([num for num in word if num.isdigit()]))
    first_letter = chr(digits)
    letter = "".join([letters for letters in word if not letters.isdigit()])
    second_letter = letter[0]
    last_letter = letter[-1]
    if len(letter) > 1:
        middle_letter = letter[1:-1]
    else:
        middle_letter = letter
    if len(letter) > 1:
        final_word = first_letter + last_letter + middle_letter + second_letter
    else:
        final_word = first_letter +last_letter
    final_list.append(final_word)
resulting_string = " ".join(final_list)
print(resulting_string)