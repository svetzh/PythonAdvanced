str_nums = [int(x) for x in input().split()]
stack = []

for _ in range(len(str_nums)):
    stack.append(str_nums.pop())
stack = " ".join(str(x) for x in stack)
print(stack)
