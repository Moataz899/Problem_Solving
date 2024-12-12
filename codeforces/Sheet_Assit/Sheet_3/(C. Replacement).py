N = int(input())

A = list(map(int, input().split()))

for i in A:
    
    if i < 0:
        print(2, end=' ')
        
    elif i > 0:
        print(1, end=' ')
        
    else:
        print(0, end=' ')
