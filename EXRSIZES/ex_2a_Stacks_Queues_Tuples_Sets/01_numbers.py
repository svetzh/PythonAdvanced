# # 1st variant:

# first_seq = {int(x) for x in input().split()}
# second_seq = {int(x) for x in input().split()}
#
# for _ in range(int(input())):
#     command_parts = input().split()
#     command = command_parts[0]
#     target_set = command_parts[1]
#
#     if command == "Add":
#         if target_set == "First":
#             first_seq = first_seq.union([int(x) for x in command_parts[2:]])
#         else:
#             second_seq = second_seq.union([int(x) for x in command_parts[2:]])
#     elif command == "Remove":
#         if target_set == "First":
#             first_seq = first_seq.difference([int(x) for x in command_parts[2:]])
#         else:
#             second_seq = second_seq.difference([int(x) for x in command_parts[2:]])
#     else:
#         print(first_seq.issubset(second_seq) or second_seq.issubset(first_seq))
#
# print(*sorted(first_seq), sep=", ")
# print(*sorted(second_seq), sep=", ")

####################################################################
# # 2nd variant
# first = set(int(x) for x in input().split())
# second = set(int(x) for x in input().split())
#
# for _ in range(int(input())):
#     first_command, *data = input().split()
#
#     command = first_command + " " + data.pop(0)
#
#     if command == "Add First":
#         [first.add(int(el)) for el in data]
#
#     elif command == "Add Second":
#         [second.add(int(el)) for el in data]
#
#     elif command == "Remove First":
#         [first.discard(int(el)) for el in data]
#     elif command == "Remove Second":
#         [second.discard(int(el)) for el in data]
#     else:
#         if first.issubset(second) or second.issubset(first):
#             print(True)
#         else:
#             print(False)
# print(*sorted(first), sep=", ")
# print(*sorted(second), sep=", ")
####################################################################

first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())
functions = {
    "Add First": lambda x: [first.add(el) for el in x],
    "Add Second": lambda x: [second.add(el) for el in x],
    "Remove First": lambda x: [first.discard(el) for el in x],
    "Remove Second": lambda x: [second.discard(el) for el in x],
    "Check Subset": lambda: print(True) if first.issubset(second) or second.issubset(first) else print(False)
}

for _ in range(int(input())):
    first_command, *data = input().split()

    command = first_command + " " + data.pop(0)
    # command1 = first_command + " " + data[0]
    if data:
        functions[command]([int(x) for x in data])
    else:
        functions[command]()

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")





