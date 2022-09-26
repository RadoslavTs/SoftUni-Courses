# card_sequence = input()
# card_list = card_sequence.split()
# remaining_a_players = 11
# remaining_b_players = 11
# red_a_players = set()
# red_b_players = set()
# temp_card = ""
# for sequence in range(len(card_list)):
#     temp_card = card_list[sequence]
#     if "A" in card_list[sequence] and temp_card[2:4] not in red_a_players:
#         remaining_a_players -= 1
#         red_a_players.add(str(temp_card[2:4]))
#         if remaining_a_players < 7:
#             break
#     elif "B" in card_list[sequence] and temp_card[2:4] not in red_b_players:
#         remaining_b_players -= 1
#         red_b_players.add(str(temp_card[2:4]))
#         if remaining_b_players < 7:
#             break
# print(f"Team A - {remaining_a_players}; Team B - {remaining_b_players}")
# if remaining_a_players < 7 or remaining_b_players < 7:
#     print("Game was terminated")

input_list = input().split()
team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
terminated_game = False
for player in input_list:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        terminated_game = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if terminated_game:
    print("Game was terminated")