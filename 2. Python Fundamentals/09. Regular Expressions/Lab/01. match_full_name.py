import re

text = input()
search_patter = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
result = re.findall(search_patter, text)
print(" ".join(result))
