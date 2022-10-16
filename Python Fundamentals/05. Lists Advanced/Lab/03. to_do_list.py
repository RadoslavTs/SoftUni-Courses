input_string = input()
tasks = []
while input_string != "End":
    input_list = input_string.split("-")
    priority = int(input_list[0])
    current_task = input_list[1]
    tasks.append([priority, current_task])
    input_string = input()
sorted_tasks = [data[1] for data in sorted(tasks)]
print(sorted_tasks)