student_count = int(input())
grade_poor = float()
poor_count = int()
grade_mid = float()
mid_count = int()
grade_good = float()
good_count = int()
grade_very_good = float()
very_good_count = int()
total_score = float()
for sequence in range(student_count):
    grade = float(input())
    total_score += grade
    if grade >= 2 and grade <= 2.99:
        grade_poor += grade
        poor_count += 1
    elif grade <= 3.99:
        grade_mid += grade
        mid_count += 1
    elif grade <=4.99:
        grade_good += grade
        good_count += 1
    elif grade >= 5:
        grade_very_good += grade
        very_good_count += 1
top_students_perc = very_good_count / student_count * 100
good_student_perc = good_count / student_count * 100
mid_student_perc = mid_count / student_count * 100
poor_student_perc = poor_count / student_count * 100
average_score = total_score / student_count
print(f"Top students: {top_students_perc:.2f}%")
print(f"Between 4.00 and 4.99: {good_student_perc:.2f}%")
print(f"Between 3.00 and 3.99: {mid_student_perc:.2f}%")
print(f"Fail: {poor_student_perc:.2f}%")
print(f"Average: {average_score:.2f}")

