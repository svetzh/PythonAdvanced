dd = {}
numbers = [float(x) for x in input().split()]
number = 0
for number in numbers:
    if number not in dd:
        dd[number] = 0
    dd[number] += 1

for number, counts in dd.items():
    print(f"{number:.1f} - {counts} times")




