import re

text_string = input()
pattern = r'([@#])([A-Za-z]{3,})(\1)(\1)([A-Za-z]{3,})(\1)'
resulting_word_list = []
result = re.finditer(pattern, text_string)
matches_found = 0
mirror_words = {}
mirror_words_list = []
for word in result:
    resulting_word_list.append(word.group(2))
    resulting_word_list.append(word.group(5))
    matches_found = int(len(resulting_word_list) / 2)
for check in range(0, len(resulting_word_list), 2):
    if resulting_word_list[check] == resulting_word_list[check+1][::-1]:
        mirror_words[resulting_word_list[check]] = resulting_word_list[check+1]

if matches_found > 0:
    print(f"{matches_found} word pairs found!")
    if mirror_words:
        print(f"The mirror words are:")
        for word, mirror in mirror_words.items():
            word_to_append = word + " <=> " + mirror
            mirror_words_list.append(word_to_append)
        print(", ".join(mirror_words_list))
    else:
        print(f"No mirror words!")
else:
    print(f"No word pairs found!")
    print(f"No mirror words!")
