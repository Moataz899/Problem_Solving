T = int(input())

for num in range(T):
    N, C = map(str, input().split())
    N = int(N)
    
    def output(N, C):
        for j in range(N):
            print(C, end = ' ')
        print()
        
    output(N, C)
