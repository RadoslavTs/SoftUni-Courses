from collections import deque

chocolates = deque(int(x) for x in input().split(', '))
milks = deque(int(x) for x in input().split(', '))
milkshakes = 0

while chocolates and milks and milkshakes != 5:

    current_chocolate = chocolates.pop()
    current_milk = milks.popleft()

    if current_chocolate <= 0 and current_milk <= 0:
        continue
    elif current_chocolate <= 0:
        milks.appendleft(current_milk)
        continue
    elif current_milk <= 0:
        chocolates.append(current_chocolate)
    elif current_chocolate != current_milk:
        milks.append(current_milk)
        chocolates.append(current_chocolate - 5)
    else:
        milkshakes += 1


if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")
if milks:
    print(f"Milk: {', '.join(map(str, milks))}")
else:
    print("Milk: empty")
