import sys
from io import StringIO

test_input1 = """3
ABC
DEF
X!@
!
"""
test_input2 = """4
asdd
xczc
qwee
qefw
4
"""
# sys.stdin = StringIO(test_input1)
sys.stdin = StringIO(test_input2)


def find_symbol(matrix, symbol):
    for row_idx in range(n):
        for col_idx in range(n):
            if matrix_lst[row_idx][col_idx] == symbol:
                return {row_idx}, {col_idx}
    return None


n = int(input())

# matrix_str = [input() for _ in range(n)]
matrix_lst = [list(input()) for _ in range(n)]
symbol = input()

result = find_symbol(matrix_lst, symbol)

if result:
    rw_idx, cl_idx = result
    print(f"({rw_idx}, {cl_idx})")
else:
    print(f"{symbol} does not occur in the matrix")













