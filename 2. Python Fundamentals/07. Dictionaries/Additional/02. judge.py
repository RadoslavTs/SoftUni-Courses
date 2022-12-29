input_line = input()
courses_dictionary = {}
individual = {}
while input_line != "no more time":
    name, course, points = [int(x) if x.isdigit() else x for x in input_line.split(" -> ")]
    courses_dictionary[course] = courses_dictionary.get(course, {})
    courses_dictionary[course][name] = courses_dictionary[course].get(name, 0)
    if courses_dictionary[course][name] < points:
        courses_dictionary[course][name] = points
    input_line = input()
for element in courses_dictionary:
    print(f"{element}: {len(courses_dictionary[element])} participants")
    counter = 1
    for name, score in sorted(courses_dictionary[element].items(), key=lambda key_value: (-key_value[1], key_value[0])):
        print(f"{counter}. {name} <::> {score}")
        if name not in individual:
            individual[name] = score
        else:
            individual[name] += score
        counter += 1
print("Individual standings:")

for pos, (user, score) in enumerate(sorted(individual.items(), key=lambda x: (-x[1], x[0])), 1):
    print(f"{pos}. {user} -> {score}")
