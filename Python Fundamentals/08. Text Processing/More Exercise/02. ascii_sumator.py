character_one = input()
character_two = input()
input_string = input()
score = 0
lower_limit = min(ord(character_one), ord(character_two))
upper_limit = max(ord(character_one), ord(character_two))
for character in input_string:
    if lower_limit < ord(character) < upper_limit:
        score += ord(character)
print(score)