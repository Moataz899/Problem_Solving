T = int(input())

for _ in range(T):
        
    N = int(input())
    A = list(map(int, input().split()))

    min_sum = float('inf')

    for i in range(N):
        for j in range(i+1, N):
            current_sum = A[i] + A[j] + j - i
            if current_sum < min_sum :
                min_sum = current_sum
                        
    print(min_sum)
    
    