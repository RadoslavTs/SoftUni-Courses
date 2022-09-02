# bad_scores = int(input())
# current_bad_scores = 0
# current_score = ""
# pass_student = True
# total_grades = float()
# total_grades_count = int()
# last_task = ""
# task_name = ""
# while current_bad_scores < bad_scores:
#     task_name = input()
#     if task_name == "Enough":
#         break
#     current_score = input()
#     total_grades += int(current_score)
#     total_grades_count += 1
#     last_task = task_name
#     if int(current_score) <= 4:
#         current_bad_scores += 1
# if current_bad_scores >= bad_scores:
#     print(f"You need a break, {current_bad_scores} poor grades.")
# else:
#     print(f"Average score: {(total_grades / total_grades_count):.2f}")
#     print(f"Number of problems: {total_grades_count}")
#     print(f"Last problem: {last_task}")

allowed_bad_scores = int(input())
task_name = input()

total_number_grades = 0
bad_scores_accumulated = 0
total_scores_accumulated = 0
bad_score_flag = False
last_problem = ""
while task_name != "Enough":
    current_grade = float(input())
    if current_grade <= 4:
        bad_scores_accumulated += 1
    total_scores_accumulated += current_grade
    total_number_grades += 1
    last_problem = task_name
    if bad_scores_accumulated > allowed_bad_scores:
        bad_score_flag = True
        break
    task_name = input()
if bad_score_flag:
    print(f"You need a break, {bad_scores_accumulated} poor grades")
else:
    print(f"Average score: {(total_scores_accumulated / total_number_grades):.2f}")
    print(f"Number of problems: {total_number_grades}")
    print(f"Last problem: {last_problem}")
