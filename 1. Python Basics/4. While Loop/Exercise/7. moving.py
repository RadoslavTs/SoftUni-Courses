width = int(input())
length = int(input())
height = int(input())
free_space = width * length * height
stop_bool = False
while free_space > 0:
    box_count = input()
    if box_count == "Done":
        stop_bool = True
        break
    free_space -= int(box_count)
if stop_bool:
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
