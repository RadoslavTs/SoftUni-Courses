number_of_rooms = int(input())
not_enough_chairs_flag = False
free_chars_left = 0
for sequence in range(1, number_of_rooms + 1):
    input_list = input().split()
    chairs_available = len(input_list[0])
    visitors = int(input_list[1])
    if chairs_available >= visitors:
        free_chars_left += chairs_available - visitors
        continue
    else:
        not_enough_chairs_flag = True
        print(f"{visitors - chairs_available} more chairs needed in room {sequence}")
if not not_enough_chairs_flag:
    print(f"Game On, {free_chars_left} free chairs left")