import re

sentence = input().lower()
searched = input().lower()
pattern = fr'\b{searched}\b'

result = re.findall(pattern, sentence)
print(len(result))