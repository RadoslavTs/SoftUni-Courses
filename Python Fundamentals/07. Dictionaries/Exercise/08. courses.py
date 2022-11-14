command = input().split(" : ")
my_dictionary = {}
while len(command) > 1:
    course, name = command[0], command[1]
    if course not in my_dictionary:
        my_dictionary[course] = []
    my_dictionary[course].append(name)
    command = input().split(" : ")
for course in my_dictionary:
    print(f"{course}: {len(my_dictionary[course])}")
    for student in my_dictionary[course]:
        print(f"-- {student}")
