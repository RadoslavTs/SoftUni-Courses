from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

words_list = ['rose', 'tulip', 'lotus', 'daffodil']

found_word = False
found_word_index = int()

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()
    for indexing in range(len(words_list)):
        if current_vowel in words_list[indexing]:
            corrected_word = words_list[indexing].replace(current_vowel, '')
            words_list[indexing] = corrected_word
            if words_list[indexing] == '':
                found_word = True
                found_word_index = indexing
                break
        if current_consonant in words_list[indexing]:
            corrected_word = words_list[indexing].replace(current_consonant, '')
            words_list[indexing] = corrected_word
            if words_list[indexing] == '':
                found_word = True
                found_word_index = indexing
                break
    if found_word:
        break

if not found_word:
    print("Cannot find any word!")
elif found_word_index == 0:
    print("Word found: rose")
elif found_word_index == 1:
    print("Word found: tulip")
elif found_word_index == 2:
    print("Word found: lotus")
elif found_word_index == 3:
    print("Word found: daffodil")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
