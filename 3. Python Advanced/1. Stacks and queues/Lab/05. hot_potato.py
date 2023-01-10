from _collections import deque

kid_names = list(input().split())
integer_number = int(input())
players_deque = deque(kid_names)
count = 0

while len(players_deque) > 1:
    count += 1
    current_name = players_deque.popleft()

    if count == integer_number:
        print(f'Removed {current_name}')
        count = 0
    else:
        players_deque.append(current_name)


print(f'Last is {players_deque[0]}')
