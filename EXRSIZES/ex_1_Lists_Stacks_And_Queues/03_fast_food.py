from collections import deque

quantitiy_food = int(input())

orders = deque(map(int, input().split()))
if orders:
    print(max(orders))

for _ in range(len(orders)):
    if orders[0] <= quantitiy_food:
        quantitiy_food -= orders.popleft()
    else:
        break

if orders:
    result = ""
    for _ in range(len(orders)):
        result += str(orders.popleft()) + " "
    print(f"Orders left: {result}")
else:
    print(f"Orders complete")
