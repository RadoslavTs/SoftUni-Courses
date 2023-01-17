number_of_students = int(input())
students_dict = {}
for sequence in range(number_of_students):
    student, grade = input().split()
    if student not in students_dict.keys():
        students_dict[student] = []
    students_dict[student].append(float(grade))

for student, grades in students_dict.items():
    grades_string = ' '.join(map(lambda result: f'{result:.2f}', grades))
    average_grade = float()
    for grade in grades:
        average_grade += grade
    average_grade /= len(grades)
    print(f'{student} -> {grades_string} (avg: {average_grade:.2f})')
