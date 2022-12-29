from math import floor
group_size = int(input())
adventure_days = int(input())
total_coins = adventure_days * 50
for sequence in range(1, adventure_days + 1):
    if sequence % 10 == 0:
        group_size -= 2
    if sequence % 15 == 0:
        group_size += 5
    total_coins -= group_size * 2
    if sequence % 3 == 0:
        total_coins -= group_size * 3
    if sequence % 5 == 0 and sequence % 3 == 0:
        total_coins += group_size * 20
        total_coins -= group_size * 2
    elif sequence % 5 == 0:
        total_coins += group_size * 20
print(f"{group_size} companions received {floor(total_coins / group_size)} coins each.")
