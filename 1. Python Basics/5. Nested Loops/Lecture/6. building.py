floor_count = int(input())
room_count = int(input())
room_type = ""
for floors in range(floor_count, 0, -1):
    for rooms in range(room_count + 1):
        if floors == floor_count:
            room_type = "L"
        elif floors % 2 == 0:
            room_type = "O"
        else:
            room_type = "A"
        print(f"{room_type}{floors}{rooms}", end = " ")
    print()