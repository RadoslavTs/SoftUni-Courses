from math import floor
tournament_count = int(input())
starting_points = int(input())
initial_points = starting_points
winning_tournaments = int()
for sequence in range(tournament_count):
    finishing_result = input()
    if finishing_result == "W":
        starting_points += 2000
        winning_tournaments += 1
    elif finishing_result == "F":
        starting_points += 1200
    else:
        starting_points += 720
print(f"Final points: {starting_points}")
print(f"Average points: {floor(((starting_points -  initial_points) / tournament_count)):.0f}")
print(f"{(winning_tournaments / tournament_count * 100):.2f}%")