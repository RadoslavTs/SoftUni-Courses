first_word, second_word = input().split()
result = 0
if len(first_word) == len(second_word):
    for sequence in range(len(first_word)):
        result += ord(first_word[sequence]) * ord(second_word[sequence])
else:
    if len(first_word) > len(second_word):
        for sequence in range(len(second_word)):
            result += ord(first_word[sequence]) * ord(second_word[sequence])
        for sequence_two in range(len(second_word), len(first_word), 1):
            result += ord(first_word[sequence_two])
    else:
        for sequence in range(len(first_word)):
            result += ord(second_word[sequence]) * ord(first_word[sequence])
        for sequence_two in range(len(first_word), len(second_word), 1):
            result += ord(second_word[sequence_two])
print(result)
