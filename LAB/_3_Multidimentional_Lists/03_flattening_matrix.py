rows = int(input())
matrix = [[int(x) for x in input().split(", ")] for x in range(rows)]
flat = [
    num
    for row in matrix
    for num in row
]

print(flat)
