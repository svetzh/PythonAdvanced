# n = int(input())
#
# name_set = set()
# for _ in range(n):
#     name_set.add(input())
#
# [print(name) for name in name_set]
# #########################################
u = int(input())
names_set = {input() for _ in range(u)}
# [print(name) for name in names_set]
print(*names_set, sep="\n")