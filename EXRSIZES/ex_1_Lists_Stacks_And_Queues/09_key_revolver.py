from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = deque([int(b) for b in input().split()])
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())

total_cost_bullets = 0
shots_fired = 0

while bullets and locks:
    if shots_fired == gun_barrel_size:
        shots_fired = 0
        print("Reloading!")

    current_bullet = bullets.pop()
    current_lock = locks[0]
    if current_bullet <= current_lock:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    total_cost_bullets += bullet_price
    shots_fired += 1

    if shots_fired == gun_barrel_size and bullets:
        shots_fired = 0
        print("Reloading!")
    if not locks:
        break

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value - total_cost_bullets}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")

