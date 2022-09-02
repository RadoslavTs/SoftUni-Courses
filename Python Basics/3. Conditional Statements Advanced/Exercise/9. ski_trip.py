days = int(input())
room_type = input()
score = input()
nights = days - 1
cost = float()
if room_type == "room for one person":
    cost = nights * 18
elif room_type == "apartment":
    if nights < 10:
        cost = nights * 25 * 0.7
    elif nights <15:
        cost = nights * 25 * 0.65
    else:
        cost = nights * 25 * 0.5
else:
    if nights < 10:
        cost = nights * 35 * 0.9
    elif nights < 15:
        cost = nights * 35 * 0.85
    else:
        cost = nights * 35 * 0.8
if score == "positive":
    cost = cost * 1.25
else:
    cost = cost * 0.9
print(f"{cost:.2f}")