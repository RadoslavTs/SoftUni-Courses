number = int(input())
key_word = input()
my_list = []
key_word_list = []
for sequence in range(number):
    sentences = input()
    my_list.append(sentences)
    if key_word in sentences:
        key_word_list.append(sentences)

print(my_list)
print(key_word_list)