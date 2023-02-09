with open('text.txt', 'r') as file:
    text_list = file.readlines()

punctuation_symbols = ["-", ",", ".", "!", "?", "'"]

text_to_write = ''
counter = 1

with open('output.txt', 'w') as new_file:

    for text in text_list:
        letters_count = 0
        punctuation_count = 0
        punctuation = 0

        for symb in text:
            if symb.isalpha():
                letters_count += 1
            elif symb in punctuation_symbols:
                punctuation_count += 1

        new_file.write(f"Line {counter}: - {text[:-1]} ({letters_count})({punctuation_count})\n")
        counter += 1
