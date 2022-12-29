import re

results = {}
participants_list = input().split(",")
command = input()
name_pattern = r'([A-za-z])'
distance_pattern = r'([0-9])'
for participant in participants_list:
    results[participant] = 0

while command != "end of race":
    name = ""
    distance = 0
    name_list = re.findall(name_pattern, command)
    distance_list = re.findall(distance_pattern, command)
    for letter in name_list:
        name += letter
    for digit in distance_list:
        distance += int(digit)
    if name in results.keys():
        results[name] += distance
    else:
        command = input()
        continue
    command = input()
print(results)
# dict(sorted(results.items(), key=lambda item: item[1]))
# for participant in participants_list:
#     if participant in results.keys():
#         print(f"{participant}")
