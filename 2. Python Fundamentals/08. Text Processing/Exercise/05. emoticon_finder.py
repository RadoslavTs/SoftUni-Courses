input_text = input()
emotes_list = []
for sequence in range(len(input_text)):
    if input_text[sequence] == ":":
        index = sequence
        resulting_word = input_text[index:index+2:]
        emotes_list.append(resulting_word)
print("\n".join(word for word in emotes_list))
