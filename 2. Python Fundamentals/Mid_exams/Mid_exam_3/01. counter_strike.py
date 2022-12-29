initial_energy = int(input())
battle_requirement = input()
won_battles = 0
enough_flag = True
battle_counter = 1
while battle_requirement != "End of battle":
    if initial_energy < int(battle_requirement):
        enough_flag = False
        break
    else:
        initial_energy -= int(battle_requirement)
        won_battles += 1
    if battle_counter % 3 == 0:
        initial_energy += won_battles
    battle_counter += 1
    battle_requirement = input()

if enough_flag:
    print(f"Won battles: {won_battles}. Energy left: {initial_energy}")
else:
    print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
