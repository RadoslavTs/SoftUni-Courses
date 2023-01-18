from collections import deque

chocolates = deque(int(x) for x in input().split(', '))
milks = deque(int(x) for x in input().split(', '))
milkshakes = 0

while (chocolates and milks) and milkshakes < 5:
    if chocolates and milks:
        current_chocolate = chocolates.pop()
        current_milk = milks.popleft()
        if current_chocolate <= 0 and chocolates:
            current_chocolate = chocolates.pop()
        elif current_chocolate <= 0 and not chocolates:
            break
        if current_milk <= 0 and milks:
            current_milk = milks.popleft()
        elif current_milk <= 0 and not milks:
            chocolates.append(current_chocolate)
            break
    else:
        break
    if current_chocolate == current_milk:
        milkshakes += 1
    else:
        milks.append(current_milk)
        current_chocolate -= 5
        if current_chocolate > 0:
            chocolates.append(current_chocolate)

if milkshakes >= 5:
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
