from collections import deque

males = deque(int(x) for x in input().split())
females = deque(int(x) for x in input().split())
matches = 0

while males and females:
    current_male = males.pop()
    current_female = females.popleft()
    if current_male <= 0:
        females.appendleft(current_female)
        continue
    if current_female <= 0:
        males.append(current_male)
        continue

    if current_female % 25 == 0:
        females.popleft()
        males.append(current_male)
        continue
    if current_male % 25 == 0:
        males.pop()
        females.appendleft(current_female)
        continue

    if current_male == current_female:
        matches += 1
        continue
    else:
        current_male -= 2
        males.append(current_male)

reversed_males = []
for _ in range(len(males)-1, -1, -1):
    reversed_males.append(males[_])


print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(str(x) for x in reversed_males)}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print("Females left: none")