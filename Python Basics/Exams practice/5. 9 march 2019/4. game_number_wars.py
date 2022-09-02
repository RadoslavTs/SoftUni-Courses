first_player_name = input()
second_player_name = input()
first_player_score = 0
second_player_score = 0
first_player_card = input()
numbers_wars_flag = False
first_player_win_flag = False
second_player_win_flag = False
while first_player_card != "End of game":
    second_player_card = int(input())
    first_player_card = int(first_player_card)
    if first_player_card > second_player_card:
        first_player_score = first_player_score + first_player_card - second_player_card
    elif first_player_card < second_player_card:
        second_player_score = second_player_score + second_player_card - first_player_card
    else:
        numbers_wars_flag = True
        first_player_card = input()
        second_player_card = input()
        if first_player_card > second_player_card:
            first_player_win_flag = True
        else:
            second_player_win_flag = True
        break
    first_player_card = input()
if numbers_wars_flag:
    print("Number wars!")
    if first_player_win_flag:
        print(f"{first_player_name} is winner with {first_player_score} points")
    else:
        print(f"{second_player_name} is winner with {second_player_score} points")
if first_player_card == "End of game":
    print(f"{first_player_name} has {first_player_score} points")
    print(f"{second_player_name} has {second_player_score} points")
