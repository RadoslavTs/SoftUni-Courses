first_match_score = input()
second_match_score = input()
third_match_score = input()
won_games = 0
drawn_games = 0
lost_games = 0
first_match_result = int(first_match_score[0]) - int(first_match_score[2])
second_match_result = int(second_match_score[0]) - int(second_match_score[2])
third_match_result = int(third_match_score[0]) - int(third_match_score[2])
if first_match_result > 0:
    won_games += 1
elif first_match_result == 0:
    drawn_games += 1
else:
    lost_games += 1
if second_match_result > 0:
    won_games += 1
elif second_match_result == 0:
    drawn_games += 1
else:
    lost_games += 1
if third_match_result > 0:
    won_games += 1
elif third_match_result == 0:
    drawn_games += 1
else:
    lost_games += 1
print(f"Team won {won_games} games.")
print(f"Team lost {lost_games} games.")
print(f" Drawn games: {drawn_games}")
