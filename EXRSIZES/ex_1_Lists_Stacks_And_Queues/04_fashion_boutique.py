box = list(map(int, input().split()))
capacity = int(input())

counter_racks = 1
current_capacity = capacity

while box:
    cloth = box.pop()
    if current_capacity - cloth >= 0:
        current_capacity -= cloth
    else:
        counter_racks += 1
        current_capacity = capacity - cloth
print(counter_racks)
####################################################
#
# clothes = [int(x) for x in input().split()]
# capacity = int(input())5 4 8 6 3 8 7 7 9
# curent_rack_space = capacity
# racks_count = 1
#
# for _ in range(len(clothes)):
#     if curent_rack_space + int(clothes[-1]) > capacity:
#         curent_rack_space = clothes.pop()
#     elif curent_rack_space + clothes[-1] == capacity:
#         curent_rack_space = 0
#         clothes.pop()
#         if clothes:
#             racks_count += 1
#         else:
#             curent_rack_space += clothes.pop()
#
# print(racks_count)
