player_name = input()
goals_scored = 0
best_score = 0
best_player = ""
while player_name != "END":
    goals_scored = int(input())
    if goals_scored > best_score:
        best_score = goals_scored
        best_player = player_name
    if goals_scored >= 10:
        break
    player_name = input()
print(f"{best_player} is the best player!")
if best_score >= 3:
    print(f"He has scored {best_score} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_score} goals.")