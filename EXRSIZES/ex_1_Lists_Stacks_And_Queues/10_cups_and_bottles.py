from collections import deque

cups_capacity = deque([int(x) for x in input().split()])
bottles_capacity = deque([int(y) for y in input().split()])

wasted_litters = 0


while cups_capacity and bottles_capacity:
    cup_val = cups_capacity.popleft()

    while cup_val > 0 and bottles_capacity:
        bottle_val = bottles_capacity.pop()
        if bottle_val >= cup_val:
            wasted_litters += bottle_val - cup_val
            cup_val = 0
        else:
            cup_val -= bottle_val

    if not cups_capacity:
        print(f"Bottles: {' '.join(map(str, reversed(bottles_capacity)))}")
    elif not bottles_capacity:
        print(f"Cups: {' '.join(map(str, cups_capacity))}")

print(f"Wasted litters of water: {wasted_litters}")








