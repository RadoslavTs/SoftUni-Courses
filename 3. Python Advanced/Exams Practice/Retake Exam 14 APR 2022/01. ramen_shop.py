from collections import deque

ramen_bowls = deque(map(int, input().split(', ')))
customers = deque(map(int, input().split(', ')))

while ramen_bowls and customers:
    current_bowl = ramen_bowls.pop()
    current_customer = customers.popleft()

    if current_customer > current_bowl:
        current_customer -= current_bowl
        customers.appendleft(current_customer)
    elif current_customer < current_bowl:
        current_bowl -= current_customer
        ramen_bowls.append(current_bowl)
    else:
        continue

if not customers:
    print('Great job! You served all the customers.')
    if ramen_bowls:
        print(f'Bowls of ramen left: {", ".join(str(x) for x in ramen_bowls)}')
elif not ramen_bowls:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f'Customers left: {", ".join(str(x) for x in customers)}')
