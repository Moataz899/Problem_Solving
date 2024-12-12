N, Q = map(int, input().split())
A = list(map(int, input().split()))

prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i-1] + A[i-1]
    
for i in range(Q):
    l, r = map(int, input().split())
    result = prefix_sum[r] - prefix_sum[l - 1]
    print(result)
    