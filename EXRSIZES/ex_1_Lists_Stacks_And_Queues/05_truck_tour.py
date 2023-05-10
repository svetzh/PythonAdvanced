from collections import deque

pumps = int(input())
circle_road = deque()

for _ in range(pumps):
    command = [int(x) for x in input().split()]
    circle_road.append(command)

for attempt in range(pumps):
    reservoir = 0
    failed = False
    for petrol, distance in circle_road:
        reservoir += petrol - distance
        if reservoir < 0:
            failed = True
            break
    if failed:
        circle_road.append(circle_road.popleft())
    else:
        print(attempt)
        break
########################################################

pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])
pumps_cpy = pumps_data.copy()
idx = 0
gas_in_tank = 0

while pumps_cpy:
    petrol, distance = pumps_cpy.popleft()

    gas_in_tank += petrol

    if gas_in_tank - distance < 0:
        pumps_data.rotate(-1)
        pumps_cpy = pumps_data.copy()
        idx += 1
        gas_in_tank = 0
    else:
        gas_in_tank -= distance

print(idx)

