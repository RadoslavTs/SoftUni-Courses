required_height = int(input())
initial_height = required_height - 30
failed_jumps = 0
failed_height = 0
fail_flag = False
jumps_number = 0
while failed_jumps < 3:
    jump_height = int(input())
    if jump_height > initial_height:
        initial_height += 5
        failed_jumps = 0
        jumps_number += 1
    elif jump_height <= initial_height:
        failed_jumps += 1
        jumps_number += 1
    if failed_jumps == 3:
        fail_flag = True
        failed_height = jump_height
    if initial_height > required_height:
        break
if fail_flag:
    print(f"Tihomir failed at {initial_height}cm after {jumps_number} jumps.")
if not fail_flag:
    print(f"Tihomir succeeded, he jumped over {required_height}cm after {jumps_number} jumps.")
