score = int(input())
first_bonus_points = 0
second_bonus_points = 0
total_bonus_points = 0
final_score = 0
if score <= 100:
    first_bonus_points = 5
elif score > 1000:
    first_bonus_points = score * 0.1
else:
    first_bonus_points = score * 0.2
if score % 2 == 0 and score % 10 == 5:
    second_bonus_points = 3
elif score % 2 == 0:
    second_bonus_points = 1
elif score % 10 == 5:
    second_bonus_points = 2
total_bonus_points = first_bonus_points + second_bonus_points
final_score = total_bonus_points + score
print(total_bonus_points)
print(final_score)


