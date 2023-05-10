# from collections import deque
#
# chocolates = deque(int(x) for x in input().split(", "))
# cups_milk = deque(int(x) for x in input().split(", "))
#
# milkshakes = 0
#
# while milkshakes != 5 and cups_milk and chocolates:
#     chocolate = chocolates.pop()
#     cup_of_milk = cups_milk.popleft()
#
#     if chocolate <= 0 and cup_of_milk <= 0:
#         continue
#     elif chocolate <= 0:
#         cups_milk.append(cup_of_milk)
#         continue
#     elif cup_of_milk <= 0:
#         chocolates.append(chocolate)
#         continue
#
#     if chocolate == cup_of_milk:
#         milkshakes += 1
#     else:
#         cups_milk.append(cup_of_milk)
#         chocolates.append(chocolate - 5)
#
# if milkshakes == 5:
#     print("Great! You made all the chocolate milkshakes needed!")
# else:
#     print("Not enough milkshakes.")
#
# print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
# print(f"Milk: {', '.join(str(x) for x in cups_milk) or 'empty'}")

######################################################################
from collections import deque

chocolate_packages = [int(x) for x in input().split(', ')]
milk_cups = deque(int(x) for x in input().split(','))
milkshakes = 0

while chocolate_packages and milk_cups and milkshakes < 5:
    chocolate = chocolate_packages.pop()
    milk = milk_cups.popleft()

    # chocolate and milk = 0
    if chocolate <= 0 and milk <= 0:
        continue

    # chocolate = 0
    if chocolate <= 0:
        milk_cups.appendleft(milk)
        continue
    # milk = 0
    if milk <= 0:
        chocolate_packages.append(chocolate)
        continue

    if chocolate == milk:
        milkshakes += 1
    else:
        milk_cups.append(milk)
        chocolate_packages.append(chocolate - 5)


if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate_packages:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate_packages])}")
else:
    print(f"Chocolate: empty")

if milk_cups:
    print(f"Milk: {', '.join([str(x) for x in milk_cups])}")
else:
    print("Milk: empty")











