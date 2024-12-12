def Distinct_Numbers(arr):
    return len(set(arr))

N = int(input())
if N > 0: 
    A = list(map(int, input().split()))
else :
    A = []

distinct_count = Distinct_Numbers(A)

print(distinct_count)
