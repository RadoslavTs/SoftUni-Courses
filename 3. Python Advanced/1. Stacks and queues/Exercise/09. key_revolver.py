from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = deque(int(b) for b in input().split())
locks = deque(int(l) for l in input().split())
intelligence_value = int(input())
shots_fired = 0
current_barrel = barrel_size
while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    current_barrel -= 1
    if current_bullet > current_lock:
        print('Ping!')
        locks.appendleft(current_lock)
        shots_fired += 1
    else:
        print('Bang!')
        shots_fired += 1
    if current_barrel == 0 and bullets:
        print('Reloading!')
        current_barrel = barrel_size

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value - shots_fired*bullet_price}")
