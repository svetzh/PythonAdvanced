# rev_str = input()
# a = rev_str[::-1]
# print(a)

########################
original_str = 'I love python'
s = []
for c in original_str:
    # push into the stack
    s.append(c)
rev_str = ''

while s:
    value = s[-1]
    rev_str += value  # pop the top
    s.pop()
print(rev_str)