numbers = [int(x) for x in input().split()]
set_n = set()
set_m = set()

for _ in range(numbers[0]):
    y = int(input())
    set_n.add(y)
for _ in range(numbers[1]):
    z = int(input())
    set_m.add(z)

intersect = set_n & set_m
print(*intersect, sep="\n")
