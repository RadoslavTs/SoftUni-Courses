employee_info = [int(input()) for num in range(4)]
total_answers_per_hour, students_in_q = sum(employee_info[:-1]), employee_info[-1]
time_needed = 0
while students_in_q > 0:
    time_needed += 1
    if time_needed % 4 != 0:
        students_in_q -= total_answers_per_hour

print(f"Time needed: {time_needed}h.")