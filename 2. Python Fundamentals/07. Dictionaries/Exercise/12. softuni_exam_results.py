command = input().split("-")
my_dictionary = {}
courses = []
while len(command) > 1:
    if len(command) == 2:
        name = command[0]
        if name in my_dictionary:
            del my_dictionary[name]
            command = input().split("-")
            continue
    name = command[0]
    language = command[1]
    score = int(command[2])
    courses.append(language)
    if name not in my_dictionary:
        my_dictionary[name] = []
        my_dictionary[name].append(language)
        my_dictionary[name].append(score)
    else:
        if my_dictionary[name][1] < score:
            my_dictionary[name][1] = score
    command = input().split("-")
print("Results:")
for item in my_dictionary:
    print(f"{item} | {my_dictionary[item][1]}")
print("Submissions:")
counted = []
for counting in courses:
    count = courses.count(counting)
    if counting in counted:
        continue
    print(f"{counting} - {count}")
    counted.append(counting)

