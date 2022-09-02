kozunak_count = int(input())
max_points = 0
max_points_baker = ""
baker_grade = int()
for sequence in range(kozunak_count):
    baker_name = input()
    grade = input()
    while grade != "Stop":
        baker_grade += int(grade)
        grade = input()
    print(f"{baker_name} has {baker_grade} points.")
    if baker_grade > max_points:
        max_points = baker_grade
        max_points_baker = baker_name
        print(f"{baker_name} is the new number 1!")
    baker_grade = 0
print(f"{max_points_baker} won competition with {max_points} points!")