player_name = input()
field = input()
remaining_points = 301
successfull_shots = 0
unsuccessful_shots = 0
win_flag = False
while field != "Retire":
    current_score = int(input())
    if field == "Double":
        current_score *= 2
    elif field == "Triple":
        current_score *= 3
    remaining_points -= current_score
    if remaining_points > 0:
        successfull_shots += 1
    elif remaining_points == 0:
        successfull_shots += 1
        win_flag = True
        break
    else:
        remaining_points += current_score
        unsuccessful_shots += 1
    field = input()
if win_flag:
    print(f"{player_name} won the leg with {successfull_shots} shots.")
else:
    print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")