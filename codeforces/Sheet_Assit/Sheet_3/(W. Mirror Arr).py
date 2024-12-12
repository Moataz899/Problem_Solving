N, M = map(int, input().split())

for i in range(N):
    Numbers = list(map(int, input().split()))
    
    reversed_Numbers = reversed(Numbers)
    
    print(*reversed_Numbers)
    
    