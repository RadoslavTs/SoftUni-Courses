first_line = input().split()
second_line = input().split()
third_line = input().split()
first_player_win = False
second_player_win = False

# horizontal_check
if first_line[0] == first_line[1] == first_line[2]:
    if first_line[0] == "1":
        first_player_win = True
    elif first_line[0] == "2":
        second_player_win = True
if second_line[0] == second_line[1] == second_line[2]:
    if second_line[0] == "1":
        first_player_win = True
    elif second_line[0] == "2":
        second_player_win = True
if third_line[0] == third_line[1] == third_line[2]:
    if third_line[0] == "1":
        first_player_win = True
    elif third_line[0] == "2":
        second_player_win = True

# vertical_check
if first_line[0] == second_line[0] == third_line[0]:
    if first_line[0] == "1":
        first_player_win = True
    elif first_line[0] == "2":
        second_player_win = True
if first_line[1] == second_line[1] == third_line[1]:
    if first_line[1] == "1":
        first_player_win = True
    elif first_line[1] == "2":
        second_player_win = True
if first_line[2] == second_line[2] == third_line[2]:
    if first_line[2] == "1":
        first_player_win = True
    elif first_line[2] == "2":
        second_player_win = True

# diagonal_check
if first_line[0] == second_line[1] == third_line[2]:
    if first_line[0] == "1":
        first_player_win = True
    elif first_line[0] == "2":
        second_player_win = True
if first_line[2] == second_line[1] == third_line[0]:
    if first_line[2] == "1":
        first_player_win = True
    elif first_line[2] == "2":
        second_player_win = True
if (first_player_win and second_player_win) or (not first_player_win and not second_player_win):
    print("Draw!")
elif first_player_win and not second_player_win:
    print("First player won")
elif not first_player_win and second_player_win:
    print("Second player won")
