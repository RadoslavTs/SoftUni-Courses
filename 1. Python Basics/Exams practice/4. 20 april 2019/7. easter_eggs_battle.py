player_one_eggs = int(input())
player_two_eggs = int(input())
player_one_end = False
player_two_end = False
end_break = False
winner = ""
while winner != "End":
    winner = input()
    if winner == "End":
        end_break = True
        break
    if winner == "one":
        player_two_eggs -= 1
    else:
        player_one_eggs -= 1
    if player_one_eggs == 0:
        player_one_end = True
        break
    elif player_two_eggs == 0:
        player_two_end = True
        break
if player_one_end:
    print(f"Player one is out of eggs. Player two has {player_two_eggs} eggs left.")
elif player_two_end:
    print(f"Player two is out of eggs. Player one has {player_one_eggs} eggs left.")
elif end_break:
    print(f"Player one has {player_one_eggs} eggs left.")
    print(f"Player two has {player_two_eggs} eggs left.")
