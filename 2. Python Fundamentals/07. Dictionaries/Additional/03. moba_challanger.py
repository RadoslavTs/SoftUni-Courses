command = input()
player_dict = {}
while command != "Season end":
    command_list = command.split(" -> ")
    if len(command_list) > 1:
        player, position, skill = [int(x) if x.isdigit() else x for x in command_list]
        player_dict[player] = player_dict.get(player, {})
        player_dict[player][position] = player_dict[player].get(position, 0)
        if player_dict[player][position] < skill:
            player_dict[player][position] = skill
    else:
        command_list = command.split(" vs ")
        player_one, player_two = [x for x in command_list]
        if player_one in player_dict.keys() and player_two in player_dict.keys():
            for key in player_dict[player_one]:
                for jey in player_dict[player_two]:
                    if key == jey:
                        if player_dict[player_one][key] > player_dict[player_two][jey]:
                            del player_dict[player_two]
                        elif player_dict[player_one][key] < player_dict[player_two][jey]:
                            del player_dict[player_one]
    command = input()
candidates = {name: sum(player_dict[name].values()) for name in player_dict}

for name, value in sorted(candidates.items(), key=lambda item: (-item[1], item[0])):
    print(f"{name}: {candidates[name]} skill")
    for pos, score in sorted(player_dict[name].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {pos} <::> {score}")
