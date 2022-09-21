input_string = input()
input_string = input_string.lower()
key_words = ["sand", "water", "fish", "sun"]
counter = 0
for word_check in key_words:
    if word_check in input_string:
        count = input_string.count(word_check)
        counter += count
        count = 0
print(counter)
