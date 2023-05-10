longest_intersection = set()


for _ in range(int(input())):
    range1, range2 = [el.split(",") for el in input().split("-")]

    range_one = set(range(int(range1[0]), int(range1[1]) + 1))
    range_two = set(range(int(range2[0]), int(range2[1]) + 1))

    intersection = range_one & range_two

    if len(longest_intersection) < len(intersection):
        longest_intersection = intersection
print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] "
      f"with length {len(longest_intersection)}")

