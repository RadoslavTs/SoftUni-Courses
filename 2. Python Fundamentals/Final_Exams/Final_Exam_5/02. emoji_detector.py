import re

input_string = input()
emoji_pattern = r'(::|\*\*)([A-Z]{1}[a-z]{2,})(\1)'
digit_pattern = r'\d'
emojis = {}
threshold = 1
emoji_list = re.finditer(emoji_pattern, input_string)
for emoji in emoji_list:
    emojis[emoji.group(2)] = emoji.group(1)
digits = re.findall(digit_pattern, input_string)
for digit in digits:
    threshold *= int(digit)
print(f"Cool threshold: {threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for emoji, sign in emojis.items():
    current_emoji = 0
    for letter in emoji:
        current_emoji += ord(letter)
    if current_emoji >= threshold:
        print(f"{sign}{emoji}{sign}")
