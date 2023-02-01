def students_credits(*args):
    credits_acquired = 0
    passed = {}
    go_no_go = ''
    for course in args:
        course_split = course.split('-')
        course_name = course_split[0]
        course_credits = int(course_split[1])
        max_test_points = int(course_split[2])
        earned_points = int(course_split[3])
        earned_credits = course_credits * (earned_points / max_test_points)
        credits_acquired += earned_credits
        passed[course_name] = earned_credits


    if credits_acquired >= 240:
        go_no_go = f"Diyan gets a diploma with {credits_acquired:.1f} credits.\n"
    else:
        go_no_go = f"Diyan needs {(240 - credits_acquired):.1f} credits more for a diploma.\n"

    for cour, cred in sorted(passed.items(), key=lambda x: -x[1]):
        go_no_go += f"{cour} - {cred:.1f}\n"

    return go_no_go


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)



