def Print(N):
    for i in range(1, N + 1):
        print(i, end=' ' if i < N else '')
        i += 1
        
N = int(input())
Print(N)
