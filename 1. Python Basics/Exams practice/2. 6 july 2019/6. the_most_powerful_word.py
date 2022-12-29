word = input()
length = 0
sum_score = 0
best_score = 0
best_word = ''
control_letter = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
while word != "End of words":
    length = len(word)
    for sequence in range(len(word)):
        sum_score += int(ord(word[sequence]))
    if word[0] in control_letter:
        sum_score *= length
    else:
        sum_score /= length
    if sum_score > best_score:
        best_score = sum_score
        best_word = word
    sum_score = 0
    length = 0
    word = input()
print(f"The most powerful word is {best_word} - {best_score}")



