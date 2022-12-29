words_count = int(input())
synonyms = {}
for words in range(words_count):
    word = input()
    synonym_word = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym_word)
for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")
