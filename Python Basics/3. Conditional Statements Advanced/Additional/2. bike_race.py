juniors = int(input())
seniors = int(input())
race_type = input()
juniors_tax = float()
seniors_tax = float()
discount = 1
income = float()
expenses = 0
if race_type == "trail":
    juniors_tax = 5.5
    seniors_tax = 7
elif race_type == "cross-country":
    juniors_tax = 8
    seniors_tax = 9.5
elif race_type == "downhill":
    juniors_tax = 12.25
    seniors_tax = 13.75
else:
    juniors_tax = 20
    seniors_tax = 21.5
if juniors + seniors >= 50 and race_type == "cross-country":
    discount = 0.75
collected_sum = (juniors_tax * juniors + seniors_tax * seniors) * discount
expenses  = collected_sum * 0.05
profit = collected_sum - expenses
print(f"{profit:.2f}")
