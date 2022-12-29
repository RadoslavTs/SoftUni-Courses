import re

input_text = input()
name_pattern = r'name is ([A-Z][a-z]+ [A-Z][a-z]+)'
age_pattern = r' (\d+) years'
year_pattern = r'on (\d{2}-\d{2}-\d{4}).'
people_dict = {}
while input_text != "make migrations":
    people = re.search(name_pattern, input_text)
    age = re.search(age_pattern, input_text)
    year = re.search(year_pattern, input_text)
    if people and age and year:
        person = people.group(1)
        old = age.group(1)
        if 9 < int(old) < 100:
            pass
        else:
            input_text = input()
            continue
        born = year.group(1)
        people_dict[person] = [old, born]
    input_text = input()
if people_dict:
    for person, info in people_dict.items():
        print(f"Name of the person: {person}.")
        if info:
            print(f"Age of the person: {info[0]}.")
            print(f"Birthdate of the person: {info[1]}.")
        else:
            print("DB is empty")
else:
    print("DB is empty")
