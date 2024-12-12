N = int(input())

grid = [['*' for _ in range(N)] for _ in range(N)]

for i in range(N):
    grid[i][i] = '\\'        
    grid[i][N-i-1] = '/'     

middle = N // 2
grid[middle][middle] = 'X'

for row in grid:
    print(''.join(row))
