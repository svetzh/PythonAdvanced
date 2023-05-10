def is_vip(guest):
    return guest[0].isdigit()


n = int(input())

vip = set()
regular = set()

for _ in range(n):
    reservation = input()

    if is_vip(reservation):
        vip.add(reservation)
    else:
        regular.add(reservation)


came_to_party = input()
while came_to_party != "END":
    if is_vip(came_to_party):
        vip.remove(came_to_party)
    else:
        regular.remove(came_to_party)
    came_to_party = input()

no_show = vip.union(regular)
print(len(no_show))
print(*sorted(no_show), sep="\n")