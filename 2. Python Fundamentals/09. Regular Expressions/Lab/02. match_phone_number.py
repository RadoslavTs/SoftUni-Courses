import re

phone_numbers = input()
search_patter = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'
result = re.findall(search_patter, phone_numbers)
print(result)
