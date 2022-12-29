from math import floor
tournament_count = int(input())
initial_points = int(input())
total_wins = 0
total_finals = 0
total_semi_finals = 0
gained_points = 0
for tournaments in range(tournament_count):
    achievement = input()
    if achievement == "W":
        total_wins += 1
        gained_points += 2000
    elif achievement == "F":
        total_finals += 1
        gained_points += 1200
    else:
        total_semi_finals += 1
        gained_points += 720
average_points = gained_points / tournament_count
perc_win = total_wins / tournament_count * 100
end_points = initial_points + gained_points
print(f"Final points: {end_points}")
print(f"Average points: {floor(average_points):.0f}")
print(f"{perc_win:.2f}%")