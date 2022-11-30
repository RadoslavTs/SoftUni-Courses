import re

input_text = input()

search_term = r"(^|(?<=\s))([a-zA-Z0-9])+([\.\-\_][A-Za-z0-9]+)*@([A-Za-z-]+)\.([A-Za-z-]+)([\.A-Za-z-])*(\b|(?=\s))"

result = re.finditer(search_term, input_text)
for mail in result:
    print(mail[0])