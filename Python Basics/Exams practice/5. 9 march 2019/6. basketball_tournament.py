tournament_name = input()
win_match = 0
lose_match = 0
total_matches = 0
while tournament_name != "End of tournaments":
    match_count = int(input())
    for sequence in range(1, match_count + 1):
        desi_points = int(input())
        enemy_team_points = int(input())
        difference = abs(desi_points - enemy_team_points)
        if desi_points > enemy_team_points:
            print(f"Game {sequence} of tournament {tournament_name}: win with {difference} points.")
            win_match += 1
        elif desi_points < enemy_team_points:
            print(f"Game {sequence} of tournament {tournament_name}: lost with {difference} points.")
            lose_match += 1
        total_matches += 1
    tournament_name = input()
win_rate = win_match / total_matches * 100
lose_rate = lose_match / total_matches * 100
print(f"{win_rate:.2f}% matches win")
print(f"{lose_rate:.2f}% matches lost")