T = int(input())

for i in range(T):
    X, Y = list(map(int, input().split()))
    
    if X > Y :
        X, Y = Y, X
        
    Sum = 0
    
    for j in range(X + 1, Y):
        if j % 2 != 0:
            Sum += j
            
    print(Sum)
            