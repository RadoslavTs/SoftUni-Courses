working_day_events = input().split("|")
energy = 100
coins = 100
completed = True
for event in working_day_events:
    event_info = event.split("-")
    if event_info[0] == "rest":
        temporary_energy = energy
        energy += int(event_info[1])
        if energy > 100:
            energy = 100
        gained_energy = energy - temporary_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event_info[0] == "order":
        if energy >= 30:
            coins += int(event_info[1])
            energy -= 30
            print(f"You earned {int(event_info[1])} coins.")
        else:
            energy += 50
            print("You had to rest!")
            continue
    else:
        if coins >= int(event_info[1]):
            print(f"You bought {event_info[0]}.")
            coins -= int(event_info[1])
        else:
            print(f"Closed! Cannot afford {event_info[0]}.")
            completed = False
            break
if completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")