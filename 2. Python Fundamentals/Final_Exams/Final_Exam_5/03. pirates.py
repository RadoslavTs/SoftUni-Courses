input_command = input()
cities = {}

while input_command != "Sail":
    input_command_split = input_command.split("||")
    city = input_command_split[0]
    population = int(input_command_split[1])
    gold = int(input_command_split[2])
    city_info = [population, gold]
    if city not in cities.keys():
        cities[city] = city_info
    else:
        cities[city][0] += population
        cities[city][1] += gold
    input_command = input()

input_actions = input()

while input_actions != "End":
    input_actions_split = input_actions.split("=>")
    action_command = input_actions_split[0]

    if action_command == "Plunder":
        city = input_actions_split[1]
        people = int(input_actions_split[2])
        gold = int(input_actions_split[3])
        if city in cities.keys():

            cities[city][0] -= people
            cities[city][1] -= gold
            if cities[city][0] <= 0 and cities[city][1] <= 0:
                print(f"{city} plundered! {gold+cities[city][1]} gold stolen, {people+cities[city][0]} citizens killed.")
                print(f"{city} has been wiped off the map!")
                del cities[city]
            elif cities[city][0] <= 0:
                print(f"{city} plundered! {gold} gold stolen, {people+cities[city][0]} citizens killed.")
                print(f"{city} has been wiped off the map!")
                del cities[city]
            elif cities[city][1] <= 0:
                print(f"{city} plundered! {gold+cities[city][1]} gold stolen, {people} citizens killed.")
                print(f"{city} has been wiped off the map!")
                del cities[city]
            else:
                print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")

    elif action_command == "Prosper":
        gold = int(input_actions_split[2])
        city = input_actions_split[1]
        if city in cities.keys():
            if gold >= 0:
                cities[city][1] += gold
                print(f"{gold} gold added to the city treasury. {city} now has {cities[city][1]} gold.")

            else:
                print("Gold added cannot be a negative number!")

    input_actions = input()
if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city in cities:
        print(f"{city} -> Population: {cities[city][0]} citizens, Gold: {cities[city][1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
