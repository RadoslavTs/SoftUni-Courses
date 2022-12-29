import re

dates = input()
search_pattern = r"(\b\d{2}\b)([\/.-])([A-Z]{1}[a-z]{2})\b\2(\d{4}\b)"
result = re.finditer(search_pattern, dates)
for element in result:
    day = element.group(1)
    month = element.group(3)
    year = element.group(4)
    print(f"Day: {day}, Month: {month}, Year: {year}")


