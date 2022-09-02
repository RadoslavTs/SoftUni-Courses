moves_count = int(input())
score = float()
from_0_to_9 = int()
from_10_to_19 = int()
from_20_to_29 = int()
form_30_to_39 = int()
from_39_to_50 = int()
invalid_numbers = int()
from_0_to_9_perc = float()
from_10_to_19_perc = float()
from_20_to_29_perc = float()
form_30_to_39_perc = float()
from_39_to_50_perc = float()
invalid_numbers_perc = float()
for sequence in range(moves_count):
    number = int(input())
    if number >= 0 and number < 10:
        score += number * 0.2
        from_0_to_9 += 1
    elif number > 0 and number < 20:
        score += number * 0.3
        from_10_to_19 += 1
    elif number > 0 and number < 30:
        score += number * 0.4
        from_20_to_29 += 1
    elif number > 0 and number < 40:
        score += 50
        form_30_to_39 += 1
    elif number > 0 and number <= 50:
        score += 100
        from_39_to_50 += 1
    else:
        score /= 2
        invalid_numbers += 1
from_0_to_9_perc = from_0_to_9 / moves_count * 100
from_10_to_19_perc = from_10_to_19 / moves_count * 100
from_20_to_29_perc = from_20_to_29 / moves_count * 100
form_30_to_39_perc = form_30_to_39 / moves_count * 100
from_39_to_50_perc = from_39_to_50 / moves_count * 100
invalid_numbers_perc = invalid_numbers / moves_count * 100
print(f"{score:.2f}")
print(f"From 0 to 9: {from_0_to_9_perc:.2f}%")
print(f"From 10 to 19: {from_10_to_19_perc:.2f}%")
print(f"From 20 to 29: {from_20_to_29_perc:.2f}%")
print(f"From 30 to 39: {form_30_to_39_perc:.2f}%")
print(f"From 40 to 50: {from_39_to_50_perc:.2f}%")
print(f"Invalid numbers: {invalid_numbers_perc:.2f}%")
