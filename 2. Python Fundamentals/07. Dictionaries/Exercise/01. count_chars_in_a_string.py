word_input = input()
character_dictionary = {}
for character in word_input:
    if character != " ":
        if character not in character_dictionary:
            character_dictionary[character] = 0
        character_dictionary[character] += 1
for character in character_dictionary:
    print(f"{character} -> {character_dictionary[character]}")
