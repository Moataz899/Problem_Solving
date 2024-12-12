N = int(input())
A = list(map(int, input().split()))


min_num = A.index(min(A))
max_num = A.index(max(A))
    
A[max_num], A[min_num] = A[min_num], A[max_num]
 
print(*A)

