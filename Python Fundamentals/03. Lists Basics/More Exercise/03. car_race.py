track_length = input().split()
middle = len(track_length) // 2
left_driver_time = 0
right_driver_time = 0
for left_side in range(0, middle):
    if int(track_length[left_side]) == 0:
        left_driver_time *= 0.8
    else:
        left_driver_time += int(track_length[left_side])
for right_side in range(len(track_length) - 1, middle, -1):
    if int(track_length[right_side]) == 0:
        right_driver_time *= 0.8
    else:
        right_driver_time += int(track_length[right_side])
if left_driver_time < right_driver_time:
    print(f"The winner is left with total time: {left_driver_time:.1f}")
else:
    print(f"The winner is right with total time: {right_driver_time:.1f}")