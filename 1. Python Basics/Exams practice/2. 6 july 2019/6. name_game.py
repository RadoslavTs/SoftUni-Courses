player_name = input()
score = 0
best_player = ""
top_score = 0
total_score = 0
while player_name != "Stop":
    for sequence in range(len(player_name)):
        score = int(input())
        if score == int(ord(player_name[sequence])):
            total_score += 10
        else:
            total_score += 2
    if top_score <= total_score:
        top_score = total_score
        best_player = player_name
    total_score = 0
    score = 0
    player_name = input()
print(f"The winner is {best_player} with {top_score} points!")




