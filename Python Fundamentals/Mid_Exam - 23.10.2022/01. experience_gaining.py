needed_experience = float(input())
battle_count = int(input())
gained_experience = float()
win_flag = False
battle_counter = 0
for sequence in range(1, battle_count + 1):
    experience_to_gain = float(input())
    battle_counter += 1
    if sequence % 3 == 0:
        experience_to_gain += 0.15 * experience_to_gain
    if sequence % 5 == 0:
        experience_to_gain -= 0.1 * experience_to_gain
    if sequence % 15 == 0:
        experience_to_gain += 0.05 * experience_to_gain
    gained_experience += experience_to_gain
    if gained_experience >= needed_experience:
        win_flag = True
        break
difference = needed_experience - gained_experience
if win_flag:
    print(f"Player successfully collected his needed experience for {battle_counter} battles.")
else:
    print(f"Player was not able to collect the needed experience, {difference:.2f} more needed.")
