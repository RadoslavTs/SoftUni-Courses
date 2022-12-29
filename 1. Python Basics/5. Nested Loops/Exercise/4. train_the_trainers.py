judge_count = int(input())
presentation_name = input()
current_grade = 0
accumulated_grade = 0
presentation_counter = 0
current_grade_average = float()
while presentation_name != "Finish":
    for grade in range(1, judge_count + 1):
        grade_judge = float(input())
        current_grade += grade_judge
    average_grade = current_grade / judge_count
    accumulated_grade += average_grade
    print(f"{presentation_name} - {average_grade:.2f}.")
    current_grade = 0
    presentation_name = input()
    presentation_counter += 1
acuumulated_grade_average = accumulated_grade / presentation_counter
print(f"Student's final assessment is {acuumulated_grade_average:.2f}.")

