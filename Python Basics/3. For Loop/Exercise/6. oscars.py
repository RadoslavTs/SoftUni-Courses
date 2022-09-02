actor = input()
academy_points = float(input())
number_of_judges = int(input())
final_score = academy_points
for sequence in range(number_of_judges):
    judge_name = input()
    judge_score = float(input())
    final_score = ((len(judge_name) * judge_score) / 2) + final_score
    if final_score >= 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {final_score:.1f}!")
        break
difference = 1250.5 - final_score
if final_score < 1250.5:
    print(f"Sorry, {actor} you need {difference:.1f} more!")
