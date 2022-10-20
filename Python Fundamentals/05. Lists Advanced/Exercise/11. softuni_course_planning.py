def add_lesson(list_of_lessens, title):
    if title not in list_of_lessens:
        list_of_lessens.append(title)
    return list_of_lessens


def insert_lesson(list_of_lessons, title, index):
    if title not in list_of_lessons:
        list_of_lessons.insert(index, title)
    return list_of_lessons


def remove_lesson(list_of_lessens, title):
    if title in list_of_lessens:
        title_index = list_of_lessens.index(title)
        if title_index + 1 in range(len(list_of_lessens)):
            if "Exercise" in list_of_lessens[title_index + 1]:
                list_of_lessens.pop(title_index + 1)
        list_of_lessens.remove(title)


def swap_lesson(list_of_lessons, first_lesson, second_lesson):
    if first_lesson in list_of_lessons and second_lesson in list_of_lessons:
        first_position = list_of_lessons.index(first_lesson)
        second_position = list_of_lessons.index(second_lesson)
        first_has_exercise = False
        second_has_exercise = False
        if first_position+1 in range(len(list_of_lessons)):
            first_has_exercise = "Exercise" in list_of_lessons[first_position+1]
        if second_position+1 in range(len(list_of_lessons)):
            second_has_exercise = "Exercise" in list_of_lessons[second_position+1]
        list_of_lessons[first_position], list_of_lessons[second_position] = list_of_lessons[second_position], list_of_lessons[first_position]
        if first_has_exercise and second_has_exercise:
            list_of_lessons[first_position + 1, second_position + 1] = list_of_lessons[second_position + 1, first_position + 1]
        elif not first_has_exercise and second_has_exercise:
            list_of_lessons.insert(first_position + 1, list_of_lessons.pop(second_position + 1))
        elif first_has_exercise and not second_has_exercise:
            list_of_lessons.insert(second_position + 1, list_of_lessons.pop(first_position + 1))
    return list_of_lessons


def exercise_lesson(list_of_lessons, title):
    if title in list_of_lessons and f"{title}-Exercise" not in list_of_lessons:
        lesson_index = list_of_lessons.index(title)
        list_of_lessons.insert(lesson_index + 1, f"{title}-Exercise")
    elif title not in list_of_lessons:
        list_of_lessons.append(title)
        list_of_lessons.append(f"{title}-Exercise")
    return list_of_lessons


lessons = input().split(", ")
command = input().split(":")
while command[0] != "course start":
    action = command[0]
    lesson_title = command[1]
    if len(command) > 2:
        lesson_title_or_index = command[2]
    if action == "Add":
        lesson = add_lesson(lessons, lesson_title)
    elif action == "Insert":
        lesson = insert_lesson(lessons, lesson_title, int(lesson_title_or_index))
    elif action == "Remove":
        lesson = remove_lesson(lessons, lesson_title)
    elif action == "Swap":
        lesson = swap_lesson(lessons, lesson_title, lesson_title_or_index)
    elif action == "Exercise":
        lesson = exercise_lesson(lessons, lesson_title)
    command = input().split(":")
for index, lesson_name in enumerate(lessons):
    print(f"{index + 1}.{lesson_name}")
