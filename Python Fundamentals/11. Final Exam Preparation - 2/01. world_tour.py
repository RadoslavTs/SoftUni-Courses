course = input()

command = input()
while command != "Travel":
    action = command.split(":")[0]
    if action == "Add Stop":
        index = int(command.split(":")[1])
        if index < len(course):
            destination = command.split(":")[2]
            course = course[:index] + destination + course[index:]
            print(course)
    elif action == "Remove Stop":
        start_index = int(command.split(":")[1])
        end_index = int(command.split(":")[2])
        if start_index < len(course) and end_index < len(course):
            course = course[:start_index] + course[end_index+1:]
        print(course)
    elif action == "Switch":
        old_string = command.split(":")[1]
        new_string = command.split(":")[2]
        while old_string in course:
            course = course.replace(old_string, new_string)
        print(course)
    command = input()
print(f"Ready for world tour! Planned stops: {course}")
