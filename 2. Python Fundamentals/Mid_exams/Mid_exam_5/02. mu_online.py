initial_health = 100
initial_bitcoins = 0
dungeon_rooms = input().split("|")
room_reached = 0
killed_flag = False
for room in dungeon_rooms:
    room_reached += 1
    room_list = room.split()
    action = room_list[0]
    value = int(room_list[1])
    if action == "potion":
        healed = 0
        if initial_health < 100:
            if initial_health + value < 100:
                healed = value
                initial_health += healed
            else:
                healed = 100 - initial_health
                initial_health = 100
        elif initial_health == 100:
            healed = 0
        print(f"You healed for {healed} hp.")
        print(f"Current health: {initial_health} hp.")
    elif action == "chest":
        initial_bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        if initial_health > value:
            initial_health -= value
            print(f"You slayed {action}.")
        else:
            print(f"You died! Killed by {action}." )
            print(f"Best room: {room_reached}")
            killed_flag = True
            break
if not killed_flag:
    print(f"You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")