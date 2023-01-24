from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar_queue = deque(int(x) for x in input().split())
check_symbols = deque(input().split())

honey = 0
operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}

while working_bees and nectar_queue:
    current_bee = working_bees.popleft()
    current_nectar = nectar_queue.pop()
    if current_nectar < current_bee:
        working_bees.appendleft(current_bee)
        continue

    symbol = check_symbols.popleft()

    if current_nectar > 0:
        honey += abs(operators[symbol](current_bee, current_nectar))


print(f"Total honey made: {honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar_queue:
    print(f"Nectar left: {', '.join(str(x) for x in nectar_queue)}")
