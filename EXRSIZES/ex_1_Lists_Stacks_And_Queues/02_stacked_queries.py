n = int(input())
stack = []

for _ in range(n):
    command = input()

    if command[0] == "1":
        num = int(command.split()[1])
        stack.append(num)
    elif command[0] == "2":
        num = stack.pop()
    elif command[0] == "3":
        print(max(stack))
    elif command[0] == "4":
        print(min(stack))
print(", ".join(map(str, stack)))