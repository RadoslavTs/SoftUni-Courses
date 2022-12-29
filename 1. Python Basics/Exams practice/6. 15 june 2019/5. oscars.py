actor_name = input()
academy_points = float(input())
judge_count = int(input())
judge_score = 0
for sequence in range(judge_count):
    judge_name = input()
    judge_points = float(input())
    judge_score = len(judge_name) * judge_points / 2
    academy_points += judge_score
    if academy_points > 1250.5:
        break
    judge_score = 0
if academy_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
else:
    difference = 1250.5 - academy_points
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")

