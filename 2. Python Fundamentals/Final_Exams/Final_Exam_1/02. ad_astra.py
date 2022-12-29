import re

text_string = input()

pattern = r'([\||#])([A-za-z ]+\1[\d]{2}\/[\d]{2}\/[\d]{2}\1[\d]+)\1'

match = re.finditer(pattern, text_string)
result_list = []
for result in match:
    result_list.append(result.group(2))

calories_per_day = 2000
total_calories = 0
for entry in result_list:
    calories = 0
    if "#" in entry:
        split_entry = entry.split("#")
        calories = int(split_entry[2])
    elif "|" in entry:
        split_entry = entry.split("|")
        calories = int(split_entry[2])
    total_calories += calories

lasting_days = total_calories // calories_per_day
print(f"You have food to last you for: {lasting_days} days!")

for item in result_list:
    calories = 0
    item_name = ""
    expiration_date = ""
    if "#" in item:
        split_entry = item.split("#")
        item_name = split_entry[0]
        expiration_date = split_entry[1]
        calories = int(split_entry[2])
    elif "|" in item:
        split_entry = item.split("|")
        item_name = split_entry[0]
        expiration_date = split_entry[1]
        calories = int(split_entry[2])
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")
