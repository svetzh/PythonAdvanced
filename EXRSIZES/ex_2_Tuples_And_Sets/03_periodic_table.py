# count_lines = int(input())
# chem_lst = []
#
# for _ in range(count_lines):
#     compounds = input().split()
#     chem_lst.append(compounds)

# # 1st variant: Flatten List of Lists + Set Comprehension
# chem_set = {i for lst in chem_lst for i in lst}
# print(*chem_set, sep="\n")

# # 2nd variant: Loop + Convert + Add Tuples
# set_chemicals = set()
# for y in chem_lst:
#     set_chemicals.add(tuple(y))
# print(set_chemicals)

# #3rd variant: Generator Expression + set() + tuple()
# set_comp_chemicals = set(tuple(x) for x in chem_lst)
# print(*set_comp_chemicals)

# #4th variant: Set Comprehension + tuple()
# st_compr = {str(x) for x in chem_lst}
# print(" ".join(*st_compr))

###################################################
n = int(input())
elements = set()

for i in range(n):
    compound = input().split()
    for element in compound:
        elements.add(element)

for element in elements:
    print(element)