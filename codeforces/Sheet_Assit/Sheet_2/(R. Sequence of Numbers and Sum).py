while True :    
    N, M = map(int, input().split())
    
    if N <= 0 or M <= 0 :
        break
    
    if N > M :
        N, M = M, N
        
    sequence = list(range(N, M + 1))
    
    Sum = sum(sequence)
    
    print(' '.join(map(str, sequence)), f"sum ={Sum}")
    