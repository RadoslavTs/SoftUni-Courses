from collections import deque

string_input = deque(input().split())
colors = {'red', 'yellow', 'blue', 'green', 'purple', 'orange'}
found = []
req_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}

}
while string_input:
    first_string = string_input.popleft()
    second_string = string_input.pop() if string_input else ''
    for color in (first_string+second_string, second_string+first_string):
        if color in colors:
            found.append(color)
            break
    else:
        for el in (first_string[:-1], second_string[:-1]):
            if el:
                string_input.insert(len(string_input)//2, el)

for color in set(req_colors.keys()).intersection(found):
    if not req_colors[color].issubset(found):
        found.remove(color)

print(found)

