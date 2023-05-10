number_usernames = int(input())
names = set(input() for _ in range(number_usernames))
print(*names, sep="\n")
