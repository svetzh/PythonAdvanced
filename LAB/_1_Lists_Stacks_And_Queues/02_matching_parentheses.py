expression = input()

s = []
for i in range(len(expression)):
    ch = expression[i]
    if ch == "(":
        s.append(i)
    elif ch == ")":
        start_idx = s.pop()
        end_idx = i
        print(expression[start_idx:end_idx + 1])

