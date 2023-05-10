from collections import deque
# water_quantity = int(input())
# people = deque()
#
# while True:
#     command = input()
#     if command == "Start":
#         break
#     people.append(command)
#
# while True:
#     command = input()
#     if command == "End":
#         break
#     elif command.startswith("refill "):
#         params = command.split()
#         water_quantity += int(params[1])
#     else:
#         person = people.popleft()
#         water_wanted = int(command)
#
#         if water_wanted <= water_quantity:
#             print(f"{person} got water")
#             water_quantity -= water_wanted
#         else:
#             print(f"{person} must wait")
# print(f"{water_quantity} liters left")
#############################################

liters = int(input())
name = input()
line = deque()
while not name == "Start":
    line.append(name)
    name = input()

command = input()

while command != "End":
    if command.isdigit():
        required_liters = int(command)
        name = line.popleft()
        if liters >= required_liters:
            liters -= required_liters
            print(f"{name} got water")
        else:
            print(f"{name} must wait")
    else:
        _, liters_to_fill = command.split()
        liters_to_fill = int(liters_to_fill)
        liters += liters_to_fill
    command = input()

print(f"{liters} liters left")