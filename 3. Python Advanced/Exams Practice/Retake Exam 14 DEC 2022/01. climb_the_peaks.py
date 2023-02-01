from collections import deque

food_portions = deque(input().split(", "))
stamina = deque(input().split(", "))

peaks = deque(["Vihren", "Kutelo", "Banski Suhodol", "Polezhan", "Kamenitza"])

peaks_dict = {
    "Vihren": 80,
    "Kutelo": 90,
    "Banski Suhodol": 100,
    "Polezhan": 60,
    "Kamenitza": 70
}

conquered_peaks = []
day = 1

while day < 8:
    current_food = int(food_portions.pop())
    current_stamina = int(stamina.popleft())
    if peaks:
        current_peak = peaks.popleft()
    else:
        break
    if current_food + current_stamina >= peaks_dict[current_peak]:
        conquered_peaks.append(current_peak)
    else:
        peaks.appendleft(current_peak)

    day += 1

if not peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if conquered_peaks:
    print("Conquered peaks:")
    print(*conquered_peaks, sep='\n')
