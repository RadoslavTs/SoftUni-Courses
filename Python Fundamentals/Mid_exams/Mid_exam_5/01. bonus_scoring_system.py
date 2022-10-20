from math import ceil
students_number = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
winner_attendance = 0
for attendance in range(students_number):
    student_attendance = int(input())
    total_bonus = student_attendance / total_number_of_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = ceil(total_bonus)
        winner_attendance = student_attendance
print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {winner_attendance} lectures.")