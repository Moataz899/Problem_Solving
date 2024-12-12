def swap_rows(matrix, x, y):
    matrix[x - 1], matrix[y - 1] = matrix[y - 1], matrix[x - 1]
    return matrix

def swap_columns(matrix, x, y):
    for row in matrix:
        row[x - 1], row[y - 1] = row[y - 1], row[x - 1]
    return matrix

N, A, B = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(N)]

matrix = swap_rows(matrix, A, B)

matrix = swap_columns(matrix, A, B)

for row in matrix:
    print(' '.join(map(str, row)))