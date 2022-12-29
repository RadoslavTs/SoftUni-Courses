number_of_snowballs = int(input())
best_snowball_weight = 0
best_snowball_time = 0
best_snowball_quality = 0
snowball_best = 0
for sequence in range(number_of_snowballs):
    snowball_weight = int(input())
    target_time = int(input())
    snowball_quality = int(input())
    snowball_current = (snowball_weight / target_time) ** snowball_quality
    if snowball_current > snowball_best:
        snowball_best = snowball_current
        best_snowball_weight = snowball_weight
        best_snowball_time = target_time
        best_snowball_quality = snowball_quality
print(f"{best_snowball_weight} : {best_snowball_time} = {snowball_best:.0f} ({best_snowball_quality})")