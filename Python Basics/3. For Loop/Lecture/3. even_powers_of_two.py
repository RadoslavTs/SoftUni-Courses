number = int(input())
for power in range(0, number + 1, 1):
    if power % 2 == 0:
        print(2 ** power)