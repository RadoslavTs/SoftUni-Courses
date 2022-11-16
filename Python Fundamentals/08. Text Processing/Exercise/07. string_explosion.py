input_text = input()
resulting_text = input_text
exploding_range_index = 0
leftover = 0
for sequence in range(len(input_text)):
    if input_text[sequence] == ">":
        explosion_index = sequence
        explosion_strength = int(input_text[explosion_index+1]) + leftover
        for sequence_two in range(explosion_index+1, len(input_text), 1):
            if input_text[sequence_two] == ">":
                exploding_range_index = sequence_two
                break
        word_to_delete_length = exploding_range_index - (explosion_index + 1)
        if word_to_delete_length >= explosion_strength:
            word_to_remove = input_text[explosion_index+1:explosion_index+2]
            leftover = 0
        else:
            word_to_remove = input_text[explosion_index+1:exploding_range_index+1]
            leftover = explosion_strength - word_to_delete_length
        resulting_text = input_text.replace(word_to_remove, "")
print(input_text)
