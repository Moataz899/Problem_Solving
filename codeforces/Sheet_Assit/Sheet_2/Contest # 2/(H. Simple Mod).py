def output(N):
    N = int(N)
    for X in range(int(N**0.5) + 1):
        xSquare = (X * X) % N
        ySquare = (N - xSquare) % N
        
        if ySquare == 0:
            return X, 0

        Y = int(ySquare ** 0.5)
        if Y * Y == ySquare and X < Y:
            return X, Y
    return None 

N = int(input())
Output = output(N)

if Output:
    print(Output[0], Output[1])
else:
    print("No solution")
