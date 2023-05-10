# from collections import deque
#
# parentheses = deque(input())
# open_parenths = deque()
#
# while parentheses:
#     left_parentheses = parentheses.popleft()
#
#     if left_parentheses in "{[(":
#         open_parenths.append(left_parentheses)
#     elif not open_parenths:
#         print("NO")
#         break
#     elif f"{open_parenths.pop() + left_parentheses}" not in "{}[]()":
#         print("NO")
#         break
# else:
#     print("YES")

#####################################################################

parentheses = input()
is_balanced = True
opening = []

mirror = {"{": "}", "[": "]", "(": ")"}

for p in parentheses:
    if p in "{[(":
        opening.append(p)
    else:
        if not opening:
            is_balanced = False
            break
        current_opening_p = opening.pop()
        if not mirror[current_opening_p] == p:
            is_balanced = False
            break
if is_balanced:
    print("YES")
else:
    print("NO")

