number_of_students = int(input())
my_dictionary = {}
for sequence in range(number_of_students):
    name = input()
    grade = float(input())
    if name not in my_dictionary:
        my_dictionary[name] = []
        my_dictionary[name].append(0)
        my_dictionary[name].append(0)
    if name in my_dictionary:
        my_dictionary[name][1] += 1
    my_dictionary[name][0] += grade
for student in my_dictionary:
    average_score = my_dictionary[student][0] / my_dictionary[student][1]
    if average_score >= 4.5:
        print(f"{student} -> {average_score:.2f}")
