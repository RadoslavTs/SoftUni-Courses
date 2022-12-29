text = input()
sum_score = int()
for number in text:
    if number == "a":
        sum_score += 1
    elif number == "e":
        sum_score += 2
    elif number == "i":
        sum_score += 3
    elif number == "o":
        sum_score += 4
    elif number == "u":
        sum_score += 5
print(sum_score)
