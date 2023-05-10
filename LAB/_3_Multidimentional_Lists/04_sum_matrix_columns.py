def get_col_sums(matrix):
    col_sums = [0] * cols_count

    for row_idx in range(rows_count):
        for col_idx in range(cols_count):
            col_sums[col_idx] += matrix[row_idx][col_idx]
    return col_sums


def get_col_sums2(matrix):
    columns_sums = []
    for col_idx in range(cols_count):
        columns_sums.append(0)
        for row_idx in range(rows_count):
            columns_sums[-1] += matrix[row_idx][col_idx]
    return columns_sums


rows_count, cols_count = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows_count):
    matrix.append(
        [int(x) for x in input().split(" ")]
    )

[print(x) for x in get_col_sums(matrix)]
[print(x) for x in get_col_sums2(matrix)]