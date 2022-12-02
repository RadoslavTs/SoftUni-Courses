course = input()

command = input()
while command != "Travel":
    command_split = command.split(":")
    action = command_split[0]
    if action == "Add Stop":
        index = int(command_split[1])
        if 0 <= index < len(course):
            destination = command_split[2]
            course = course[:index] + destination + course[index:]
    elif action == "Remove Stop":
        start_index = int(command_split[1])
        end_index = int(command_split[2])
        if 0 <= start_index < len(course) and 0 <= end_index < len(course):
            course = course[:start_index] + "" + course[end_index + 1:]
    elif action == "Switch":
        old_string = command_split[1]
        new_string = command_split[2]
        if old_string in course:
            course = course.replace(old_string, new_string)
    print(course)
    command = input()
print(f"Ready for world tour! Planned stops: {course}")