import re

search_pattern = r"\d+"

while True:
    input_string = input()
    if input_string:
        result = re.findall(search_pattern, input_string)
        for show in result:
            print(show, end=" ")
    else:
        break
