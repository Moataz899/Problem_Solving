def check_neighbors(N, M, grid, X, Y):
    X, Y = X - 1, Y - 1  

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for dx, dy in directions:
        nx, ny = X + dx, Y + dy
        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != 'x':
            print("no")
            return
    print("yes")

N, M = map(int, input().split())
grid = [input() for _ in range(N)]
X, Y = map(int, input().split())

check_neighbors(N, M, grid, X, Y)
