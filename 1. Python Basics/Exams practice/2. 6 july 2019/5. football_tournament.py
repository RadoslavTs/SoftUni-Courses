team_name = input()
games_played = int(input())
total_score = 0
total_wins = 0
total_ds = 0
total_ls = 0
if games_played > 0:
    for sequence in range(games_played):
        score = input()
        if score == "W":
            total_score += 3
            total_wins += 1
        elif score == "D":
            total_score += 1
            total_ds += 1
        else:
            total_ls += 1
        win_rate = total_wins / games_played * 100
    print(f"{team_name} has won {total_score} points during this season.")
    print("Total stats:")
    print(f"## W: {total_wins}")
    print(f"## D: {total_ds}")
    print(f"## L: {total_ls}")
    print(f"Win rate: {win_rate:.2f}%")
else:
    print(f"{team_name} hasn't played any games during this season.")
