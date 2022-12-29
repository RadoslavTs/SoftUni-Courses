def check_the_rooms(number_of_rooms):
    free_chars_left = 0
    needed_chairs = 0
    for sequence in range(1, number_of_rooms + 1):
        input_list = input().split()
        chairs_available = len(input_list[0])
        visitors = int(input_list[1])
        if chairs_available >= visitors:
            free_chars_left += chairs_available - visitors
        else:
            needed_chairs += visitors - chairs_available
            print(f"{visitors - chairs_available} more chairs needed in room {sequence}")
    return free_chars_left, needed_chairs


number_of_rooms = int(input())
total_free_chairs, total_needed_chairs = check_the_rooms(number_of_rooms)
if total_free_chairs >= total_needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
