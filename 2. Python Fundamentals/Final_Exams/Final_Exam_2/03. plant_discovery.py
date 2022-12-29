number = int(input())
plants_dict = {}
for sequence in range(number):
    input_line = input().split("<->")
    plant_type = input_line[0]
    plant_rarity = int(input_line[1])
    plants_dict[plant_type] = [plant_rarity, []]

command = input()
while command != "Exhibition":
    command_split = command.split(": ")
    action = command_split[0]
    plant_info_split = command_split[1].split(" - ")
    plant = plant_info_split[0]
    if plant not in plants_dict.keys():
        print("error")
    else:
        if action == "Rate":
            rating = int(plant_info_split[1])
            plants_dict[plant][1].append(rating)
        elif action == "Update":
            rarity = plant_info_split[1]
            plants_dict[plant][0] = rarity
        elif action == "Reset":
            plants_dict[plant][1].clear()
    command = input()
print("Plants for the exhibition:")
for plant in plants_dict.keys():
    average_rating = 0
    if plants_dict[plant][1]:
        for rating in plants_dict[plant][1]:
            average_rating += rating
        average_rating = average_rating / len(plants_dict[plant][1])
    print(f"- {plant}; Rarity: {plants_dict[plant][0]}; Rating: {average_rating:.2f}")
