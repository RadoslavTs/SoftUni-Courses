name = input()
total_score = float()
total_grades = 0
breaks = 0
while breaks <= 1 and total_grades <= 11:
    current_grade = float(input())
    if current_grade < 4:
        breaks += 1
        total_score += current_grade
    total_grades += 1
    total_score += current_grade
average_score = total_score / total_grades
if breaks > 1:
    print(f"{name} has been excluded at {total_grades - 1} grade")
else:
    print(f"{name} graduated. Average grade: {average_score:.2f}")

# name = input()
# total_score = float()
# total_grades = 0
# breaks = 0
# for sequence in range(1, 13):
#     current_grade = float(input())
#     if current_grade < 4:
#         breaks += 1
#         total_score += current_grade
#     if breaks > 1:
#         break
#     total_grades += 1
#     total_score += current_grade
# average_score = total_score / total_grades
# if breaks > 1:
#     print(f"{name} has been excluded at {total_grades} grade")
# else:
#     print(f"{name} graduated. Average grade: {average_score:.2f}")