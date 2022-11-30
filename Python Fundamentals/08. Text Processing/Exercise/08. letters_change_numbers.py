input_list = input().split()
result = 0
current_number = 0
for word in input_list:
    word_to_check = word.strip()
    current_score = 0
    current_number = int(word[1:-1])
    if word_to_check[0].isupper():
        letter_position = ord(word_to_check[0]) - 64
        current_score = current_number / letter_position
    else:
        letter_position = ord(word_to_check[0]) - 96
        current_score = current_number * letter_position
    if word_to_check[-1].isupper():
        letter_position = ord(word_to_check[-1]) - 64
        current_score -= letter_position
    else:
        letter_position = ord(word_to_check[-1]) - 96
        current_score += letter_position
    result += current_score
print(f"{result:.2f}")
