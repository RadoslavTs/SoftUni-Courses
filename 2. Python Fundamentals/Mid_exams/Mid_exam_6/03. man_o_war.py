def fire_action(index_to_hit, damage):
    if 0 <= index_to_hit < len(war_ship_status):
        war_ship_status[index_to_hit] -= damage
        if war_ship_status[index_to_hit] <= 0:
            print(f"You won! The enemy ship has sunken.")
            exit()


def defend_action(starting_index, ending_index, damage):
    if 0 <= starting_index < len(pirate_ship_status) and 0 <= ending_index < len(pirate_ship_status):
        for fight in range(starting_index, ending_index + 1):
            pirate_ship_status[fight] -= damage
            if pirate_ship_status[fight] <= 0:
                print(f"You lost! The pirate ship has sunken.")
                exit()


def repair_action(index_to_repair, health_to_restore):
    if 0 <= index_to_repair < len(pirate_ship_status):
        pirate_ship_status[index_to_repair] += health_to_restore
        if pirate_ship_status[index_to_repair] > max_health:
            pirate_ship_status[index_to_repair] = max_health


def status_action():
    section_to_repair = 0
    for section in pirate_ship_status:
        if section < 0.2 * max_health:
            section_to_repair += 1
    return section_to_repair


pirate_ship_status = list(map(int, input().split(">")))
war_ship_status = list(map(int, input().split(">")))
max_health = int(input())
command = input()
while command != "Retire":
    command_list = command.split()
    action = command_list[0]
    if action == "Fire":
        index_place = int(command_list[1])
        damage_placed = int(command_list[2])
        fire_action(index_place, damage_placed)
    elif action == "Defend":
        start_place = int(command_list[1])
        end_place = int(command_list[2])
        damaged_placed = int(command_list[3])
        defend_action(start_place, end_place, damaged_placed)
    elif action == "Repair":
        index_to_use = int(command_list[1])
        health_to_use = int(command_list[2])
        repair_action(index_to_use, health_to_use)
    elif action == "Status":
        sections_that_need_repair = status_action()
        print(f"{sections_that_need_repair} sections need repair.")
    command = input()

if len(pirate_ship_status) and len(war_ship_status) > 0:
    print(f"Pirate ship status: {sum(pirate_ship_status)}")
    print(f"Warship status: {sum(war_ship_status)}")
