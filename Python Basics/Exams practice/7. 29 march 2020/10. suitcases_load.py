plane_capacity = float(input())
suitcases_count = 0
suitcase_size = input()
while suitcase_size != "End":
    suitcase_size_float = float(suitcase_size)
    suitcases_count += 1
    added_luggage = 0
    if suitcases_count % 3 == 0:
        added_luggage = suitcase_size_float * 0.1
    plane_capacity -= suitcase_size_float + added_luggage
    if plane_capacity <= 0:
        if plane_capacity != 0:
            suitcases_count -= 1
        print("No more space!")
        break
    suitcase_size = input()
    if suitcase_size == "End":
        end_flag = True
else:
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {suitcases_count} suitcases loaded.")


