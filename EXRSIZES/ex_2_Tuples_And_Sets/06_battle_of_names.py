N = int(input())
names_odd = set()
names_even = set()
for i in range(1, N + 1):
    name = input()
    ord_name = sum([ord(x) for x in name])
    devided = ord_name // i
    if devided % 2 == 0:
        names_even.add(devided)
    else:
        names_odd.add(devided)

if sum(names_odd) == sum(names_even):
    print(", ".join(map(str, (names_odd | names_even))))
elif sum(names_odd) > sum(names_even):
    print(", ".join(map(str, (names_odd - names_even))))
elif sum(names_odd) < sum(names_even):
    print(", ".join(str(x) for x in (names_odd ^ names_even)))
    #
    # {', '.join(str(x) for x in longest_intersection)}
